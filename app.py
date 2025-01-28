from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db_connection

app = Flask(__name__)

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Add Employee Route
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        department = request.form['department']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO employees (first_name, last_name, email, phone, department)'
            'VALUES (%s, %s, %s, %s, %s)',
            (first_name, last_name, email, phone, department)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('view_employees'))
    return render_template('add_employee.html')

# View Employees Route
@app.route('/view')
def view_employees():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employees;')
    employees = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('view_employees.html', employees=employees)

# Delete Employee Route
@app.route('/delete/<int:id>')
def delete_employee(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM employees WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('view_employees'))



# Update Employee Route
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        department = request.form['department']

        cur.execute(
            'UPDATE employees SET first_name = %s, last_name = %s, email = %s, phone = %s, department = %s'
            'WHERE id = %s',
            (first_name, last_name, email, phone, department, id)
        )
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('view_employees'))
    
    cur.execute('SELECT * FROM employees WHERE id = %s', (id,))
    employee = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('update_employee.html', employee=employee)


# Run the App
if __name__ == '__main__':
    app.run(debug=True)
  