// StaffSync JavaScript Functions

document.addEventListener('DOMContentLoaded', function() {
    // Initialize components
    initializeAttendanceButton();
    initializeDataTables();
    initializeCharts();
    initializeNotifications();
    
    // Auto-hide alerts after 5 seconds
    setTimeout(() => {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            setTimeout(() => alert.remove(), 300);
        });
    }, 5000);
});

// Attendance Functions
function initializeAttendanceButton() {
    const attendanceBtn = document.getElementById('attendanceBtn');
    if (attendanceBtn) {
        attendanceBtn.addEventListener('click', markAttendance);
    }
}

async function markAttendance() {
    const button = document.getElementById('attendanceBtn');
    const originalText = button.innerHTML;
    
    // Show loading state
    button.innerHTML = '<div class="spinner"></div>';
    button.disabled = true;
    
    try {
        const response = await fetch('/api/mark_attendance', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        
        const data = await response.json();
        
        if (data.success) {
            showNotification(data.message, 'success');
            updateAttendanceUI(data.type, data.time);
        } else {
            showNotification(data.message, 'error');
        }
    } catch (error) {
        showNotification('Error marking attendance. Please try again.', 'error');
        console.error('Attendance error:', error);
    } finally {
        button.innerHTML = originalText;
        button.disabled = false;
    }
}

function updateAttendanceUI(type, time) {
    const attendanceStatus = document.getElementById('attendanceStatus');
    if (attendanceStatus) {
        if (type === 'checkin') {
            attendanceStatus.innerHTML = `
                <div class="text-success">
                    <i class="fas fa-clock"></i> Checked in at ${time}
                </div>
            `;
        } else {
            attendanceStatus.innerHTML = `
                <div class="text-primary">
                    <i class="fas fa-check-circle"></i> Checked out at ${time}
                </div>
            `;
        }
    }
    
    // Refresh attendance table if visible
    const attendanceTable = document.getElementById('attendanceTable');
    if (attendanceTable) {
        setTimeout(() => location.reload(), 1000);
    }
}

// Data Tables
function initializeDataTables() {
    const tables = document.querySelectorAll('.data-table');
    tables.forEach(table => {
        // Add search functionality
        addTableSearch(table);
        
        // Add sorting
        addTableSorting(table);
        
        // Add pagination if needed
        if (table.rows.length > 20) {
            addTablePagination(table);
        }
    });
}

function addTableSearch(table) {
    const searchContainer = document.createElement('div');
    searchContainer.className = 'mb-3';
    searchContainer.innerHTML = `
        <input type="text" class="form-control" placeholder="Search..." onkeyup="filterTable(this, '${table.id}')">
    `;
    table.parentNode.insertBefore(searchContainer, table);
}

function filterTable(input, tableId) {
    const filter = input.value.toLowerCase();
    const table = document.getElementById(tableId);
    const rows = table.getElementsByTagName('tr');
    
    for (let i = 1; i < rows.length; i++) {
        const row = rows[i];
        const cells = row.getElementsByTagName('td');
        let found = false;
        
        for (let j = 0; j < cells.length; j++) {
            if (cells[j].textContent.toLowerCase().indexOf(filter) > -1) {
                found = true;
                break;
            }
        }
        
        row.style.display = found ? '' : 'none';
    }
}

function addTableSorting(table) {
    const headers = table.querySelectorAll('th');
    headers.forEach((header, index) => {
        header.style.cursor = 'pointer';
        header.addEventListener('click', () => sortTable(table, index));
    });
}

function sortTable(table, columnIndex) {
    const rows = Array.from(table.querySelectorAll('tbody tr'));
    const isAscending = table.getAttribute('data-sort-direction') !== 'asc';
    
    rows.sort((a, b) => {
        const aValue = a.cells[columnIndex].textContent.trim();
        const bValue = b.cells[columnIndex].textContent.trim();
        
        if (isNaN(aValue)) {
            return isAscending ? aValue.localeCompare(bValue) : bValue.localeCompare(aValue);
        } else {
            return isAscending ? parseFloat(aValue) - parseFloat(bValue) : parseFloat(bValue) - parseFloat(aValue);
        }
    });
    
    const tbody = table.querySelector('tbody');
    rows.forEach(row => tbody.appendChild(row));
    
    table.setAttribute('data-sort-direction', isAscending ? 'asc' : 'desc');
}

// Charts (using Chart.js if available)
function initializeCharts() {
    // Attendance Chart
    const attendanceChartCanvas = document.getElementById('attendanceChart');
    if (attendanceChartCanvas && typeof Chart !== 'undefined') {
        createAttendanceChart(attendanceChartCanvas);
    }
    
    // Payroll Chart
    const payrollChartCanvas = document.getElementById('payrollChart');
    if (payrollChartCanvas && typeof Chart !== 'undefined') {
        createPayrollChart(payrollChartCanvas);
    }
}

function createAttendanceChart(canvas) {
    const ctx = canvas.getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'Attendance',
                data: [85, 90, 88, 92, 89, 45, 30],
                borderColor: '#667eea',
                backgroundColor: 'rgba(102, 126, 234, 0.1)',
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });
}

function createPayrollChart(canvas) {
    const ctx = canvas.getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            datasets: [{
                label: 'Payroll',
                data: [65000, 68000, 67000, 69000, 71000, 70000],
                backgroundColor: 'rgba(102, 126, 234, 0.8)'
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

// Notifications
function initializeNotifications() {
    // Check for new notifications every 30 seconds
    setInterval(checkNotifications, 30000);
}

function showNotification(message, type = 'info', duration = 5000) {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} notification`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
        opacity: 0;
        transform: translateX(100%);
        transition: all 0.3s ease;
    `;
    notification.innerHTML = `
        <div class="d-flex justify-content-between align-items-center">
            <span>${message}</span>
            <button type="button" class="btn-close" onclick="closeNotification(this)">×</button>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.opacity = '1';
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Auto remove
    setTimeout(() => {
        closeNotification(notification.querySelector('.btn-close'));
    }, duration);
}

function closeNotification(button) {
    const notification = button.closest('.notification');
    notification.style.opacity = '0';
    notification.style.transform = 'translateX(100%)';
    setTimeout(() => notification.remove(), 300);
}

async function checkNotifications() {
    try {
        const response = await fetch('/api/notifications');
        const data = await response.json();
        
        if (data.notifications && data.notifications.length > 0) {
            data.notifications.forEach(notification => {
                showNotification(notification.message, notification.type);
            });
        }
    } catch (error) {
        console.error('Error checking notifications:', error);
    }
}

// Employee Management Functions
function deleteEmployee(employeeId) {
    if (confirm('Are you sure you want to delete this employee?')) {
        fetch(`/api/employees/${employeeId}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showNotification('Employee deleted successfully', 'success');
                location.reload();
            } else {
                showNotification('Error deleting employee', 'error');
            }
        })
        .catch(error => {
            showNotification('Error deleting employee', 'error');
            console.error('Error:', error);
        });
    }
}

function editEmployee(employeeId) {
    // Redirect to edit form or open modal
    window.location.href = `/admin/employees/edit/${employeeId}`;
}

// Payroll Functions
function generatePayroll(employeeId, period) {
    const data = {
        employee_id: employeeId,
        period: period
    };
    
    fetch('/api/payroll/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification('Payroll generated successfully', 'success');
            location.reload();
        } else {
            showNotification('Error generating payroll', 'error');
        }
    })
    .catch(error => {
        showNotification('Error generating payroll', 'error');
        console.error('Error:', error);
    });
}

// Modern Sidebar Toggle (Mobile)
function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const toggle = document.querySelector('.mobile-menu-toggle');
    const isOpen = sidebar.classList.contains('open');
    
    if (isOpen) {
        sidebar.classList.remove('open');
        toggle.classList.remove('active');
        toggle.querySelector('i').className = 'fas fa-bars';
        document.body.style.overflow = '';
    } else {
        sidebar.classList.add('open');
        toggle.classList.add('active');
        toggle.querySelector('i').className = 'fas fa-times';
        document.body.style.overflow = 'hidden'; // Prevent background scroll
    }
}

// Close sidebar when clicking outside (mobile)
document.addEventListener('click', function(event) {
    const sidebar = document.querySelector('.sidebar');
    const toggle = document.querySelector('.mobile-menu-toggle');
    
    if (sidebar && sidebar.classList.contains('open') && 
        !sidebar.contains(event.target) && 
        !toggle.contains(event.target)) {
        toggleSidebar();
    }
});

// Close sidebar on window resize (desktop)
window.addEventListener('resize', function() {
    if (window.innerWidth > 768) {
        const sidebar = document.querySelector('.sidebar');
        const toggle = document.querySelector('.mobile-menu-toggle');
        const staffNav = document.querySelector('.navbar-nav');
        
        if (sidebar && sidebar.classList.contains('open')) {
            sidebar.classList.remove('open');
            toggle.classList.remove('active');
            toggle.querySelector('i').className = 'fas fa-bars';
            document.body.style.overflow = '';
        }
        
        if (staffNav && staffNav.classList.contains('show')) {
            staffNav.classList.remove('show');
        }
    }
});

// Staff Mobile Menu Toggle
function toggleStaffMobileMenu() {
    const navbar = document.querySelector('.navbar-nav');
    const toggle = document.querySelector('.mobile-menu-toggle');
    const isOpen = navbar.classList.contains('show');
    
    if (isOpen) {
        navbar.classList.remove('show');
        toggle.classList.remove('active');
        toggle.querySelector('i').className = 'fas fa-bars';
    } else {
        navbar.classList.add('show');
        toggle.classList.add('active');
        toggle.querySelector('i').className = 'fas fa-times';
    }
}

// Close staff mobile menu when clicking outside
document.addEventListener('click', function(event) {
    const navbar = document.querySelector('.navbar-nav');
    const toggle = document.querySelector('.mobile-menu-toggle');
    const navContainer = document.querySelector('.navbar');
    
    if (navbar && navbar.classList.contains('show') && 
        !navContainer.contains(event.target)) {
        toggleStaffMobileMenu();
    }
});

// Form Validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    const inputs = form.querySelectorAll('input[required], select[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.classList.add('is-invalid');
            isValid = false;
        } else {
            input.classList.remove('is-invalid');
        }
    });
    
    return isValid;
}

// Date Functions
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

function formatTime(timeString) {
    if (!timeString) return '-';
    return new Date(`1970-01-01T${timeString}`).toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Export Functions
function exportToCSV(tableId, filename = 'export.csv') {
    const table = document.getElementById(tableId);
    const rows = table.querySelectorAll('tr');
    const csvContent = [];
    
    rows.forEach(row => {
        const cells = row.querySelectorAll('th, td');
        const rowData = Array.from(cells).map(cell => cell.textContent.trim());
        csvContent.push(rowData.join(','));
    });
    
    const blob = new Blob([csvContent.join('\n')], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
}

// Real-time Clock
function updateClock() {
    const clockElement = document.getElementById('currentTime');
    if (clockElement) {
        const now = new Date();
        clockElement.textContent = now.toLocaleTimeString();
    }
}

// Update clock every second
setInterval(updateClock, 1000);
updateClock(); // Initial call