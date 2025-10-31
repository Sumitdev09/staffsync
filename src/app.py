from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

DATABASE = 'staffsync.db'  # Database is in the same directory as app.py

# Decorators
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session or session.get('role') != 'admin':
            flash('Access denied. Admin privileges required.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Database functions
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    
    # Create tables
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'staff',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            position TEXT,
            department TEXT,
            salary REAL DEFAULT 0,
            hire_date TEXT,
            status TEXT DEFAULT 'Active'
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER,
            date TEXT NOT NULL,
            check_in_time TEXT,
            check_out_time TEXT,
            total_hours REAL DEFAULT 0,
            overtime_hours REAL DEFAULT 0,
            status TEXT DEFAULT 'Present',
            notes TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS payroll (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER,
            pay_period_start TEXT NOT NULL,
            pay_period_end TEXT NOT NULL,
            basic_salary REAL DEFAULT 0,
            overtime_pay REAL DEFAULT 0,
            allowances REAL DEFAULT 0,
            gross_pay REAL DEFAULT 0,
            tax_deduction REAL DEFAULT 0,
            other_deductions REAL DEFAULT 0,
            total_deductions REAL DEFAULT 0,
            net_pay REAL DEFAULT 0,
            status TEXT DEFAULT 'draft',
            processed_at TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS leaves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER,
            leave_type TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            days_count INTEGER,
            reason TEXT,
            status TEXT DEFAULT 'pending',
            applied_date TEXT DEFAULT CURRENT_TIMESTAMP,
            approved_by INTEGER,
            approved_date TEXT,
            FOREIGN KEY (employee_id) REFERENCES employees (id),
            FOREIGN KEY (approved_by) REFERENCES users (id)
        )
    ''')
    
    # Insert demo data if tables are empty
    if c.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 0:
        # Admin user
        admin_hash = generate_password_hash('admin123')
        c.execute("INSERT INTO users (username, email, password_hash, role) VALUES (?, ?, ?, ?)",
                 ('admin', 'admin@staffsync.com', admin_hash, 'admin'))
        
        # Staff users
        staff_users = [
            ('john.doe', 'john.doe@staffsync.com', 'pass123'),
            ('jane.smith', 'jane.smith@staffsync.com', 'pass123'),
            ('mike.johnson', 'mike.johnson@staffsync.com', 'pass123'),
            ('sarah.wilson', 'sarah.wilson@staffsync.com', 'pass123'),
            ('david.brown', 'david.brown@staffsync.com', 'pass123')
        ]
        
        for username, email, password in staff_users:
            password_hash = generate_password_hash(password)
            c.execute("INSERT INTO users (username, email, password_hash, role) VALUES (?, ?, ?, ?)",
                     (username, email, password_hash, 'staff'))
    
    if c.execute("SELECT COUNT(*) FROM employees").fetchone()[0] == 0:
        employees_data = [
            ('John', 'Doe', 'john.doe@staffsync.com', '555-0101', 'Software Developer', 'IT', 75000, '2023-01-15', 'Active'),
            ('Jane', 'Smith', 'jane.smith@staffsync.com', '555-0102', 'HR Manager', 'Human Resources', 65000, '2023-02-01', 'Active'),
            ('Mike', 'Johnson', 'mike.johnson@staffsync.com', '555-0103', 'Sales Representative', 'Sales', 55000, '2023-03-10', 'Active'),
            ('Sarah', 'Wilson', 'sarah.wilson@staffsync.com', '555-0104', 'Accountant', 'Finance', 60000, '2023-01-20', 'Active'),
            ('David', 'Brown', 'david.brown@staffsync.com', '555-0105', 'Marketing Specialist', 'Marketing', 58000, '2023-04-05', 'Active'),
            ('Emily', 'Davis', 'emily.davis@staffsync.com', '555-0106', 'Designer', 'Creative', 62000, '2023-05-12', 'Active'),
            ('Robert', 'Miller', 'robert.miller@staffsync.com', '555-0107', 'Project Manager', 'IT', 80000, '2023-01-08', 'Active'),
            ('Lisa', 'Garcia', 'lisa.garcia@staffsync.com', '555-0108', 'Customer Service', 'Support', 45000, '2023-06-15', 'Active'),
            ('James', 'Wilson', 'james.wilson@staffsync.com', '555-0109', 'Data Analyst', 'IT', 70000, '2023-02-28', 'Active'),
            ('Amanda', 'Taylor', 'amanda.taylor@staffsync.com', '555-0110', 'Operations Manager', 'Operations', 75000, '2023-03-22', 'Active')
        ]
        
        for emp in employees_data:
            c.execute("""INSERT INTO employees 
                        (first_name, last_name, email, phone, position, department, salary, hire_date, status) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", emp)
    
    # Add attendance records
    if c.execute("SELECT COUNT(*) FROM attendance").fetchone()[0] == 0:
        today = datetime.now().strftime('%Y-%m-%d')
        from datetime import timedelta
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        
        attendance_data = [
            # Today's attendance - mixed scenarios
            (1, today, '09:00', '17:00', 8.0, 0.0, 'present', 'On time'),
            (2, today, '09:15', '17:30', 8.25, 0.25, 'late', 'Late arrival'),
            (3, today, '08:45', '18:00', 9.25, 1.25, 'present', 'Early arrival, overtime'),
            (4, today, '09:00', '17:00', 8.0, 0.0, 'present', 'Regular hours'),
            (5, today, '09:30', '17:00', 7.5, 0.0, 'late', 'Late arrival'),
            (6, today, '09:00', None, 0.0, 0.0, 'present', 'Currently working'),
            (7, today, '09:00', '13:00', 4.0, 0.0, 'half_day', 'Half day leave'),
            (8, today, '09:00', '17:00', 8.0, 0.0, 'present', 'Regular hours'),
            (9, today, None, None, 0.0, 0.0, 'absent', 'Sick leave'),
            (10, today, '08:30', '17:30', 9.0, 1.0, 'present', 'Overtime'),
            
            # Yesterday's attendance - full day records
            (1, yesterday, '09:00', '17:00', 8.0, 0.0, 'present', 'Regular day'),
            (2, yesterday, '09:00', '17:00', 8.0, 0.0, 'present', 'Regular day'),
            (3, yesterday, '08:45', '17:15', 8.5, 0.5, 'present', 'Extra work'),
            (4, yesterday, '09:15', '17:00', 7.75, 0.0, 'late', 'Late start'),
            (5, yesterday, '09:00', '17:00', 8.0, 0.0, 'present', 'Regular day'),
            (6, yesterday, '09:00', '17:00', 8.0, 0.0, 'present', 'Regular day'),
            (7, yesterday, '09:00', '17:00', 8.0, 0.0, 'present', 'Regular day'),
            (8, yesterday, None, None, 0.0, 0.0, 'absent', 'Personal leave'),
            (9, yesterday, '09:00', '17:00', 8.0, 0.0, 'present', 'Regular day'),
            (10, yesterday, '09:00', '17:00', 8.0, 0.0, 'present', 'Regular day')
        ]
        
        for emp_id, date, check_in, check_out, total_hours, overtime_hours, status, notes in attendance_data:
            c.execute("""INSERT INTO attendance 
                        (employee_id, date, check_in_time, check_out_time, total_hours, overtime_hours, status, notes) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                     (emp_id, date, check_in, check_out, total_hours, overtime_hours, status, notes))
    
    # Add payroll records
    if c.execute("SELECT COUNT(*) FROM payroll").fetchone()[0] == 0:
        payroll_data = [
            # October 2024 payroll
            (1, '2024-10-01', '2024-10-31', 75000/12, 500, 750, 500, 150, 650, 0, 'processed'),
            (2, '2024-10-01', '2024-10-31', 65000/12, 200, 650, 400, 120, 520, 0, 'processed'),
            (3, '2024-10-01', '2024-10-31', 55000/12, 300, 550, 350, 100, 450, 0, 'paid'),
            (4, '2024-10-01', '2024-10-31', 60000/12, 150, 600, 375, 110, 485, 0, 'paid'),
            (5, '2024-10-01', '2024-10-31', 58000/12, 250, 580, 360, 105, 465, 0, 'processed'),
            
            # September 2024 payroll (completed)
            (1, '2024-09-01', '2024-09-30', 75000/12, 600, 750, 550, 160, 710, 0, 'paid'),
            (2, '2024-09-01', '2024-09-30', 65000/12, 150, 650, 420, 125, 545, 0, 'paid'),
            (3, '2024-09-01', '2024-09-30', 55000/12, 400, 550, 380, 110, 490, 0, 'paid'),
            (4, '2024-09-01', '2024-09-30', 60000/12, 200, 600, 400, 120, 520, 0, 'paid'),
            (5, '2024-09-01', '2024-09-30', 58000/12, 300, 580, 390, 115, 505, 0, 'paid'),
        ]
        
        for emp_id, start_date, end_date, basic_salary, overtime_pay, allowances, tax_deduction, other_deductions, total_deductions, net_pay, status in payroll_data:
            gross_pay = basic_salary + overtime_pay + allowances
            net_pay = gross_pay - total_deductions
            
            c.execute("""INSERT INTO payroll 
                        (employee_id, pay_period_start, pay_period_end, basic_salary, overtime_pay, allowances, 
                         gross_pay, tax_deduction, other_deductions, total_deductions, net_pay, status) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                     (emp_id, start_date, end_date, basic_salary, overtime_pay, allowances, 
                      gross_pay, tax_deduction, other_deductions, total_deductions, net_pay, status))
    
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def index():
    if 'user_id' in session:
        if session.get('role') == 'admin':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('staff_dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']
            
            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('staff_dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form.get('role', 'staff')
        
        conn = get_db_connection()
        
        # Check if username already exists
        existing_user = conn.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone()
        if existing_user:
            flash('Username already exists', 'error')
            conn.close()
            return render_template('register.html')
        
        # Create new user
        password_hash = generate_password_hash(password)
        conn.execute('INSERT INTO users (username, email, password_hash, role) VALUES (?, ?, ?, ?)',
                    (username, email, password_hash, role))
        conn.commit()
        conn.close()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))

# Admin Routes
@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    conn = get_db_connection()
    
    # Get statistics
    total_employees = conn.execute('SELECT COUNT(*) FROM employees').fetchone()[0]
    present_today = conn.execute("SELECT COUNT(*) FROM attendance WHERE date = ? AND status = 'Present'", 
                                (datetime.now().strftime('%Y-%m-%d'),)).fetchone()[0]
    total_departments = conn.execute('SELECT COUNT(DISTINCT department) FROM employees').fetchone()[0]
    
    # Recent employees
    recent_employees = conn.execute('''
        SELECT first_name, last_name, position, hire_date 
        FROM employees 
        ORDER BY id DESC LIMIT 5
    ''').fetchall()
    
    # Today's attendance
    todays_attendance = conn.execute('''
        SELECT e.first_name, e.last_name, a.check_in_time, a.check_out_time, a.status
        FROM employees e
        LEFT JOIN attendance a ON e.id = a.employee_id AND a.date = ?
        ORDER BY e.first_name
        LIMIT 10
    ''', (datetime.now().strftime('%Y-%m-%d'),)).fetchall()
    
    conn.close()
    
    return render_template('admin/dashboard.html', 
                         total_employees=total_employees,
                         present_today=present_today,
                         total_departments=total_departments,
                         recent_employees=recent_employees,
                         todays_attendance=todays_attendance)

@app.route('/admin/employees')
@admin_required
def admin_employees():
    conn = get_db_connection()
    employees = conn.execute('SELECT * FROM employees ORDER BY first_name').fetchall()
    conn.close()
    return render_template('admin/employees.html', employees=employees)

# API endpoint for employee details
@app.route('/api/employee/<int:employee_id>')
@admin_required
def get_employee_api(employee_id):
    conn = get_db_connection()
    employee = conn.execute('SELECT * FROM employees WHERE id = ?', (employee_id,)).fetchone()
    conn.close()
    
    if not employee:
        return jsonify({'error': 'Employee not found'}), 404
    
    return jsonify(dict(employee))

@app.route('/admin/employees/add', methods=['GET', 'POST'])
@admin_required
def add_employee():
    if request.method == 'POST':
        conn = get_db_connection()
        conn.execute('''INSERT INTO employees 
                       (first_name, last_name, email, phone, position, department, salary, hire_date, status)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (request.form['first_name'], request.form['last_name'], 
                     request.form['email'], request.form['phone'],
                     request.form['position'], request.form['department'],
                     float(request.form['salary']), request.form['hire_date'], 'Active'))
        conn.commit()
        conn.close()
        flash('Employee added successfully!', 'success')
        return redirect(url_for('admin_employees'))
    
    return render_template('admin/add_employee.html')

@app.route('/admin/employees/edit/<int:employee_id>', methods=['GET', 'POST'])
@admin_required
def edit_employee(employee_id):
    conn = get_db_connection()
    
    if request.method == 'POST':
        status = request.form.get('status', 'Active')
        conn.execute('''UPDATE employees SET 
                       first_name=?, last_name=?, email=?, phone=?, 
                       position=?, department=?, salary=?, status=? 
                       WHERE id=?''',
                    (request.form['first_name'], request.form['last_name'],
                     request.form['email'], request.form['phone'],
                     request.form['position'], request.form['department'],
                     float(request.form['salary']), status, employee_id))
        conn.commit()
        conn.close()
        flash('Employee updated successfully!', 'success')
        return redirect(url_for('admin_employees'))
    
    employee = conn.execute('SELECT * FROM employees WHERE id = ?', (employee_id,)).fetchone()
    conn.close()
    
    if not employee:
        flash('Employee not found', 'error')
        return redirect(url_for('admin_employees'))
    
    return render_template('admin/edit_employee.html', employee=employee)

@app.route('/admin/employees/delete/<int:employee_id>', methods=['POST'])
@admin_required
def delete_employee(employee_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})
    conn.close()
    flash('Employee deleted successfully!', 'success')
    return redirect(url_for('admin_employees'))

@app.route('/admin/attendance')
@admin_required
def admin_attendance():
    selected_date = request.args.get('date', date.today().isoformat())
    
    conn = get_db_connection()
    
    # Get all employees with their attendance for the selected date
    attendance_data = conn.execute('''
        SELECT 
            e.id as employee_id,
            e.first_name,
            e.last_name,
            e.position,
            e.department,
            a.id as attendance_id,
            a.check_in_time,
            a.check_out_time,
            a.total_hours,
            a.overtime_hours,
            a.status,
            a.notes
        FROM employees e
        LEFT JOIN attendance a ON e.id = a.employee_id AND a.date = ?
        WHERE e.status = 'Active'
        ORDER BY e.first_name, e.last_name
    ''', (selected_date,)).fetchall()
    
    # Calculate attendance statistics
    total_employees = len(attendance_data)
    present_employees = sum(1 for record in attendance_data if record['check_in_time'])
    late_employees = sum(1 for record in attendance_data if record['status'] == 'late')
    attendance_rate = (present_employees / total_employees * 100) if total_employees > 0 else 0
    
    conn.close()
    
    return render_template('admin/attendance.html', 
                         attendance_data=attendance_data,
                         selected_date=selected_date,
                         total_employees=total_employees,
                         present_employees=present_employees,
                         late_employees=late_employees,
                         attendance_rate=attendance_rate)

@app.route('/admin/payroll')
@admin_required
def admin_payroll():
    conn = get_db_connection()
    
    # Get payroll records with employee information
    payroll_records = conn.execute('''
        SELECT 
            p.id,
            p.employee_id,
            e.first_name,
            e.last_name,
            e.position,
            p.pay_period_start,
            p.pay_period_end,
            p.basic_salary,
            p.overtime_pay,
            p.allowances,
            p.gross_pay,
            p.tax_deduction,
            p.other_deductions,
            p.total_deductions,
            p.net_pay,
            p.status,
            p.created_at
        FROM payroll p
        JOIN employees e ON p.employee_id = e.id
        ORDER BY p.created_at DESC, e.first_name
    ''').fetchall()
    
    # Calculate payroll statistics
    total_gross = sum(float(record['gross_pay'] or 0) for record in payroll_records)
    total_net = sum(float(record['net_pay'] or 0) for record in payroll_records)
    pending_count = sum(1 for record in payroll_records if record['status'] == 'draft')
    
    conn.close()
    
    return render_template('admin/payroll.html', 
                         payroll_records=payroll_records,
                         total_gross=total_gross,
                         total_net=total_net,
                         pending_count=pending_count)

@app.route('/admin/departments', methods=['GET', 'POST'])
@admin_required
def admin_departments():
    conn = get_db_connection()
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form.get('description', '')
        head = request.form.get('head', '')
        budget = request.form.get('budget')
        
        # Add department logic here (would need departments table)
        flash('Department created successfully!', 'success')
        return redirect(url_for('admin_departments'))
    
    # Get department data (mock data for now)
    departments = [
        {
            'name': 'Human Resources',
            'description': 'Manages employee relations, recruitment, and HR policies',
            'head': 'Sarah Wilson',
            'budget': 150000,
            'employee_count': 5,
            'employees': [
                {'first_name': 'Sarah', 'last_name': 'Wilson'},
                {'first_name': 'Mike', 'last_name': 'Johnson'},
            ]
        },
        {
            'name': 'Information Technology',
            'description': 'Develops and maintains technology infrastructure',
            'head': 'John Doe',
            'budget': 300000,
            'employee_count': 8,
            'employees': [
                {'first_name': 'John', 'last_name': 'Doe'},
                {'first_name': 'Jane', 'last_name': 'Smith'},
            ]
        },
        {
            'name': 'Finance',
            'description': 'Handles financial planning, accounting, and budgets',
            'head': 'David Brown',
            'budget': 200000,
            'employee_count': 4,
            'employees': [
                {'first_name': 'David', 'last_name': 'Brown'},
            ]
        }
    ]
    
    all_employees = conn.execute('SELECT first_name, last_name FROM employees ORDER BY first_name').fetchall()
    total_employees = conn.execute('SELECT COUNT(*) FROM employees').fetchone()[0]
    
    conn.close()
    return render_template('admin/departments.html', 
                         departments=departments,
                         all_employees=all_employees,
                         total_employees=total_employees)

@app.route('/admin/settings', methods=['GET', 'POST'])
@admin_required
def admin_settings():
    # Mock settings data
    settings = {
        'company_name': 'StaffSync Corporation',
        'company_email': 'admin@staffsync.com',
        'company_phone': '+1 (555) 123-4567',
        'company_website': 'https://staffsync.com',
        'company_address': '123 Business Street, Suite 100\nCity, State 12345\nCountry',
        'timezone': 'America/New_York',
        'date_format': 'MM/DD/YYYY',
        'currency': 'USD',
        'working_hours': 8,
        'email_notifications': True,
        'auto_backup': True,
        'two_factor_auth': False
    }
    
    return render_template('admin/settings.html', 
                         settings=settings,
                         last_backup='2025-10-30 14:30:00')

@app.route('/admin/settings/company', methods=['POST'])
@admin_required
def update_company_settings():
    # Here you would update company settings in database
    flash('Company settings updated successfully!', 'success')
    return redirect(url_for('admin_settings'))

@app.route('/admin/settings/system', methods=['POST'])
@admin_required
def update_system_settings():
    # Here you would update system settings in database
    flash('System settings updated successfully!', 'success')
    return redirect(url_for('admin_settings'))

# Staff Routes
@app.route('/staff/dashboard')
@login_required
def staff_dashboard():
    if session.get('role') != 'staff':
        return redirect(url_for('admin_dashboard'))
    
    conn = get_db_connection()
    
    # Get employee info by matching username with email
    username = session.get('username')
    email = f"{username}@staffsync.com"
    
    employee = conn.execute('''
        SELECT id, first_name, last_name, email, phone, position, department, salary, hire_date
        FROM employees 
        WHERE email = ?
    ''', (email,)).fetchone()
    
    if not employee:
        flash('Employee profile not found. Please contact admin.', 'error')
        conn.close()
        return redirect(url_for('login'))
    
    employee_id = employee['id']
    
    # Get recent attendance
    recent_attendance = conn.execute('''
        SELECT date, check_in_time, check_out_time, status
        FROM attendance 
        WHERE employee_id = ?
        ORDER BY date DESC LIMIT 10
    ''', (employee_id,)).fetchall()
    
    # Get today's attendance
    today = datetime.now().strftime('%Y-%m-%d')
    todays_attendance = conn.execute('''
        SELECT check_in_time, check_out_time, status
        FROM attendance 
        WHERE employee_id = ? AND date = ?
    ''', (employee_id, today)).fetchone()
    
    # Calculate leave balance
    used_leaves = conn.execute('''
        SELECT COALESCE(SUM(days_count), 0) FROM leaves 
        WHERE employee_id = ? AND status = 'approved' 
        AND start_date >= date('now', 'start of year')
    ''', (employee_id,)).fetchone()[0]
    
    leave_balance = 20 - used_leaves
    
    conn.close()
    
    return render_template('staff/dashboard.html', 
                         employee=employee,
                         recent_attendance=recent_attendance,
                         todays_attendance=todays_attendance,
                         leave_balance=leave_balance)

@app.route('/staff/mark_attendance', methods=['POST'])
@login_required
def mark_attendance():
    if session.get('role') != 'staff':
        return jsonify({'success': False, 'message': 'Access denied'})
    
    action = request.form.get('action')  # 'checkin' or 'checkout'
    
    conn = get_db_connection()
    username = session.get('username')
    email = f"{username}@staffsync.com"
    
    employee = conn.execute('SELECT id FROM employees WHERE email = ?', (email,)).fetchone()
    if not employee:
        conn.close()
        return jsonify({'success': False, 'message': 'Employee not found'})
    
    employee_id = employee['id']
    today = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M')
    
    # Check if attendance record exists for today
    existing = conn.execute('SELECT * FROM attendance WHERE employee_id = ? AND date = ?', 
                          (employee_id, today)).fetchone()
    
    if action == 'checkin':
        if existing:
            conn.close()
            return jsonify({'success': False, 'message': 'Already checked in today'})
        
        conn.execute('INSERT INTO attendance (employee_id, date, check_in_time, status) VALUES (?, ?, ?, ?)',
                    (employee_id, today, current_time, 'Present'))
        message = f'Checked in at {current_time}'
    
    elif action == 'checkout':
        if not existing:
            conn.close()
            return jsonify({'success': False, 'message': 'No check-in record found for today'})
        
        if existing['check_out_time']:
            conn.close()
            return jsonify({'success': False, 'message': 'Already checked out today'})
        
        conn.execute('UPDATE attendance SET check_out_time = ? WHERE employee_id = ? AND date = ?',
                    (current_time, employee_id, today))
        message = f'Checked out at {current_time}'
    
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'message': message})

@app.route('/staff/profile', methods=['GET', 'POST'])
@login_required
def staff_profile():
    if session.get('role') != 'staff':
        return redirect(url_for('admin_dashboard'))
    
    conn = get_db_connection()
    username = session.get('username')
    email = f"{username}@staffsync.com"
    
    employee = conn.execute('''
        SELECT id, first_name, last_name, email, phone, position, department, salary, hire_date
        FROM employees WHERE email = ?
    ''', (email,)).fetchone()
    
    if not employee:
        flash('Employee profile not found.', 'error')
        conn.close()
        return redirect(url_for('staff_dashboard'))
    
    if request.method == 'POST':
        # Update profile information
        phone = request.form.get('phone')
        conn.execute('''UPDATE employees SET phone = ? WHERE id = ?''',
                    (phone, employee['id']))
        conn.commit()
        flash('Profile updated successfully!', 'success')
        conn.close()
        return redirect(url_for('staff_profile'))
    
    conn.close()
    return render_template('staff/profile.html', employee=employee)

@app.route('/staff/leave', methods=['GET', 'POST'])
@login_required
def staff_leave():
    if session.get('role') != 'staff':
        return redirect(url_for('admin_dashboard'))
    
    conn = get_db_connection()
    username = session.get('username')
    email = f"{username}@staffsync.com"
    
    employee = conn.execute('SELECT id FROM employees WHERE email = ?', (email,)).fetchone()
    if not employee:
        flash('Employee profile not found.', 'error')
        conn.close()
        return redirect(url_for('staff_dashboard'))
    
    employee_id = employee['id']
    
    if request.method == 'POST':
        leave_type = request.form.get('leave_type')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        reason = request.form.get('reason')
        
        # Calculate days
        from datetime import datetime
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        days_count = (end - start).days + 1
        
        conn.execute('''INSERT INTO leaves 
                       (employee_id, leave_type, start_date, end_date, days_count, reason)
                       VALUES (?, ?, ?, ?, ?, ?)''',
                    (employee_id, leave_type, start_date, end_date, days_count, reason))
        conn.commit()
        flash(f'Leave application submitted successfully for {days_count} days!', 'success')
        conn.close()
        return redirect(url_for('staff_leave'))
    
    # Get leave history
    leave_history = conn.execute('''
        SELECT * FROM leaves WHERE employee_id = ? ORDER BY applied_date DESC
    ''', (employee_id,)).fetchall()
    
    # Calculate leave balance (assume 20 days annual leave)
    used_leaves = conn.execute('''
        SELECT COALESCE(SUM(days_count), 0) FROM leaves 
        WHERE employee_id = ? AND status = 'approved' 
        AND start_date >= date('now', 'start of year')
    ''', (employee_id,)).fetchone()[0]
    
    leave_balance = 20 - used_leaves
    
    conn.close()
    return render_template('staff/leave.html', 
                         leave_history=leave_history, 
                         leave_balance=leave_balance)

# API Routes
@app.route('/api/notifications')
def api_notifications():
    """Simple notifications endpoint to prevent 404 errors"""
    return jsonify({
        'notifications': [],
        'count': 0
    })

@app.route('/api/employee/<int:employee_id>')
@admin_required
def api_employee(employee_id):
    conn = get_db_connection()
    employee = conn.execute('SELECT * FROM employees WHERE id = ?', (employee_id,)).fetchone()
    conn.close()
    
    if employee:
        return jsonify(dict(employee))
    return jsonify({'error': 'Employee not found'}), 404

# Attendance Management API
@app.route('/api/attendance/mark_present', methods=['POST'])
@admin_required
def mark_employee_present():
    data = request.get_json()
    employee_id = data.get('employee_id')
    date = data.get('date', datetime.now().strftime('%Y-%m-%d'))
    check_in_time = data.get('check_in_time', datetime.now().strftime('%H:%M'))
    
    conn = get_db_connection()
    
    # Check if attendance record already exists
    existing = conn.execute('''
        SELECT id FROM attendance WHERE employee_id = ? AND date = ?
    ''', (employee_id, date)).fetchone()
    
    if existing:
        # Update existing record
        conn.execute('''
            UPDATE attendance 
            SET check_in_time = ?, status = 'present', updated_at = CURRENT_TIMESTAMP
            WHERE employee_id = ? AND date = ?
        ''', (check_in_time, employee_id, date))
    else:
        # Create new record
        conn.execute('''
            INSERT INTO attendance (employee_id, date, check_in_time, status)
            VALUES (?, ?, ?, 'present')
        ''', (employee_id, date, check_in_time))
    
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'message': 'Attendance marked successfully'})

@app.route('/api/attendance/edit', methods=['POST'])
@admin_required
def edit_attendance():
    data = request.get_json()
    employee_id = data.get('employee_id')
    date = data.get('date')
    check_in_time = data.get('check_in_time')
    check_out_time = data.get('check_out_time')
    status = data.get('status', 'present')
    notes = data.get('notes', '')
    
    # Calculate total hours if both times are provided
    total_hours = 0
    if check_in_time and check_out_time:
        try:
            checkin = datetime.strptime(check_in_time, '%H:%M')
            checkout = datetime.strptime(check_out_time, '%H:%M')
            # Handle cases where checkout is next day
            if checkout < checkin:
                checkout = checkout.replace(day=checkout.day + 1)
            total_hours = (checkout - checkin).total_seconds() / 3600
        except:
            total_hours = 0
    
    conn = get_db_connection()
    
    # Check if record exists
    existing = conn.execute('''
        SELECT id FROM attendance WHERE employee_id = ? AND date = ?
    ''', (employee_id, date)).fetchone()
    
    if existing:
        # Update existing record
        conn.execute('''
            UPDATE attendance 
            SET check_in_time = ?, check_out_time = ?, total_hours = ?, 
                status = ?, notes = ?, updated_at = CURRENT_TIMESTAMP
            WHERE employee_id = ? AND date = ?
        ''', (check_in_time, check_out_time, total_hours, status, notes, employee_id, date))
    else:
        # Create new record
        conn.execute('''
            INSERT INTO attendance (employee_id, date, check_in_time, check_out_time, 
                                  total_hours, status, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (employee_id, date, check_in_time, check_out_time, total_hours, status, notes))
    
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'message': 'Attendance updated successfully'})

# Payroll Management API
@app.route('/api/payroll/generate', methods=['POST'])
@admin_required
def generate_payroll():
    data = request.get_json()
    pay_period_start = data.get('pay_period_start')
    pay_period_end = data.get('pay_period_end')
    employee_selection = data.get('employee_selection', 'all')
    include_overtime = data.get('include_overtime', True)
    include_tax = data.get('include_tax', True)
    
    conn = get_db_connection()
    
    # Get employees based on selection
    if employee_selection == 'all':
        employees = conn.execute('''
            SELECT id, first_name, last_name, salary, position
            FROM employees WHERE status = 'Active'
        ''').fetchall()
    else:
        # For now, just handle 'all' - can extend for department/individual selection
        employees = conn.execute('''
            SELECT id, first_name, last_name, salary, position
            FROM employees WHERE status = 'Active'
        ''').fetchall()
    
    payroll_created = 0
    
    for employee in employees:
        employee_id = employee['id']
        basic_salary = float(employee['salary'] or 0)
        
        # Calculate attendance-based adjustments
        if include_overtime:
            # Get total hours worked in the pay period
            attendance_hours = conn.execute('''
                SELECT SUM(total_hours) as total_hours, SUM(overtime_hours) as overtime_hours
                FROM attendance 
                WHERE employee_id = ? AND date BETWEEN ? AND ?
            ''', (employee_id, pay_period_start, pay_period_end)).fetchone()
            
            overtime_hours = float(attendance_hours['overtime_hours'] or 0)
            # Assuming overtime rate is 1.5x hourly rate
            hourly_rate = basic_salary / (30 * 8)  # Approximate hourly rate
            overtime_pay = overtime_hours * hourly_rate * 1.5
        else:
            overtime_pay = 0
        
        # Calculate allowances (can be customized based on position/department)
        allowances = basic_salary * 0.1  # 10% of basic salary as allowances
        
        # Calculate gross pay
        gross_pay = basic_salary + overtime_pay + allowances
        
        # Calculate deductions
        if include_tax:
            tax_rate = 0.2 if gross_pay > 5000 else 0.15  # Progressive tax
            tax_deduction = gross_pay * tax_rate
        else:
            tax_deduction = 0
        
        other_deductions = gross_pay * 0.02  # 2% for insurance/benefits
        total_deductions = tax_deduction + other_deductions
        
        # Calculate net pay
        net_pay = gross_pay - total_deductions
        
        # Check if payroll already exists for this period
        existing_payroll = conn.execute('''
            SELECT id FROM payroll 
            WHERE employee_id = ? AND pay_period_start = ? AND pay_period_end = ?
        ''', (employee_id, pay_period_start, pay_period_end)).fetchone()
        
        if not existing_payroll:
            # Create new payroll record
            conn.execute('''
                INSERT INTO payroll (
                    employee_id, pay_period_start, pay_period_end,
                    basic_salary, overtime_pay, allowances, gross_pay,
                    tax_deduction, other_deductions, total_deductions, net_pay,
                    status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'draft')
            ''', (employee_id, pay_period_start, pay_period_end, basic_salary, 
                 overtime_pay, allowances, gross_pay, tax_deduction, 
                 other_deductions, total_deductions, net_pay))
            
            payroll_created += 1
    
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True, 
        'message': f'Payroll generated for {payroll_created} employees',
        'payroll_created': payroll_created
    })

@app.route('/api/payroll/<int:payroll_id>/process', methods=['POST'])
@admin_required
def process_payroll(payroll_id):
    conn = get_db_connection()
    
    # Update payroll status to processed
    conn.execute('''
        UPDATE payroll 
        SET status = 'processed', processed_at = CURRENT_TIMESTAMP, 
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ? AND status = 'draft'
    ''', (payroll_id,))
    
    affected_rows = conn.total_changes
    conn.commit()
    conn.close()
    
    if affected_rows > 0:
        return jsonify({'success': True, 'message': 'Payroll processed successfully'})
    else:
        return jsonify({'success': False, 'message': 'Payroll not found or already processed'})

@app.route('/api/payroll/<int:payroll_id>/mark_paid', methods=['POST'])
@admin_required
def mark_payroll_paid(payroll_id):
    conn = get_db_connection()
    
    # Update payroll status to paid
    conn.execute('''
        UPDATE payroll 
        SET status = 'paid', updated_at = CURRENT_TIMESTAMP
        WHERE id = ? AND status = 'processed'
    ''', (payroll_id,))
    
    affected_rows = conn.total_changes
    conn.commit()
    conn.close()
    
    if affected_rows > 0:
        return jsonify({'success': True, 'message': 'Payroll marked as paid successfully'})
    else:
        return jsonify({'success': False, 'message': 'Payroll not found or not in processed state'})

@app.route('/api/payroll/<int:payroll_id>')
@admin_required
def get_payroll_details(payroll_id):
    conn = get_db_connection()
    
    payroll = conn.execute('''
        SELECT 
            p.*,
            e.first_name,
            e.last_name,
            e.position,
            e.email
        FROM payroll p
        JOIN employees e ON p.employee_id = e.id
        WHERE p.id = ?
    ''', (payroll_id,)).fetchone()
    
    conn.close()
    
    if payroll:
        return jsonify(dict(payroll))
    else:
        return jsonify({'error': 'Payroll record not found'}), 404

if __name__ == '__main__':
    print("🚀 Starting StaffSync Employee Management System...")
    print("=" * 60)
    print("📋 Login Credentials:")
    print("   👑 Admin - Username: admin, Password: admin123")
    print("   👤 Staff - Username: john.doe, Password: pass123")
    print("   👤 Staff - Username: jane.smith, Password: pass123")
    print("   👤 Staff - Username: mike.johnson, Password: pass123")
    print("   👤 Staff - Username: sarah.wilson, Password: pass123")
    print("   👤 Staff - Username: david.brown, Password: pass123")
    print("🌐 Access URL: http://localhost:5000")
    print("📝 Registration: http://localhost:5000/register")
    print("=" * 60)
    
    # Initialize database
    init_database()
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)