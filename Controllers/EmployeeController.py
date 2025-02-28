from Connectors.MySqlConnections import hrm_db_connection
class EmployeeController:

    def AuthLogin(EmpData):

        conn = hrm_db_connection()
        
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)

                query = "SELECT EMP_ID, EMP_PASSWORD, EMP_ROLE, EMP_DEPARTMENT, EMP_POSITION, EMP_NAME, EMP_GENDER, EMP_BIRTHDATE, EMP_ADDRESS, EMP_PHONE, EMP_EMAIL, EMP_PIC, EMP_STATUS FROM `hrm-system-db`.tbl_employee WHERE EMP_ID = %s AND EMP_PASSWORD = %s;"

                cursor.execute(query, (EmpData.EMP_ID, EmpData.EMP_PASSWORD))

                result = cursor.fetchone()

                if result:
                    return {"status": 200, "data": result}
                else:
                    return {"status": 401, "message": "Invalid email or password"}
                
            except Exception as e:

                return {"status": 500, "message": f"Error: {e}"}
            
            finally:
                if cursor:
                    cursor.close()
                if conn.is_connected():
                    conn.close()

            
        return {"status": 500, "message": "Database connection failed"}
    
    def FetchEmployee(EmpData):
        
        conn = hrm_db_connection()
        
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)

                query = "SELECT EMP_ID, EMP_PASSWORD, EMP_ROLE, EMP_DEPARTMENT, EMP_POSITION, EMP_NAME, EMP_GENDER, EMP_BIRTHDATE, EMP_ADDRESS, EMP_PHONE, EMP_EMAIL, EMP_PIC, EMP_STATUS FROM `hrm-system-db`.tbl_employee WHERE EMP_ID LIKE %s;"
                
                cursor.execute(query, (f"%{EmpData.EMP_ID}%",))

                result = cursor.fetchall()

                if result:
                    return {"status": 200, "data": result}
                else:
                    return {"status": 404, "message": "No data found"}
                
            except Exception as e:

                return {"status": 500, "message": f"Error: {e}"}
            
            finally:
                if cursor:
                    cursor.close()
                if conn.is_connected():
                    conn.close()

            
        return {"status": 500, "message": "Database connection failed"}
                