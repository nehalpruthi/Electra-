from flask import Flask, request, render_template,redirect
import pymysql
import pymysql.cursors

app = Flask(__name__)

# Create a global variable for the database connection
db_connection = None

def initialize_db_connection(username, password):
    global db_connection
    try:
        # Establish a connection to the MySQL database
        db_connection = pymysql.connect(host='localhost',
                                         user=username,
                                         password=password,
                                         cursorclass=pymysql.cursors.DictCursor)
        print("Database connection established successfully.")
    except pymysql.Error as e:
        print(f"Error connecting to database: {e}")

@app.route('/')
def index():
    return render_template('first.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    # Initialize the database connection
    initialize_db_connection(username, password)

    if db_connection:
        # Create a cursor object to execute SQL queries
        with db_connection.cursor() as cursor:
            # Example: Execute a SELECT query
            sql_query = "USE ELECTION;" 
            cursor.execute(sql_query)
            # result = cursor.fetchall() # Fetch all rows from the query result

        return render_template('second.html')
    else:
        error_message = "Error connecting to database"
        return render_template('error.html', error_message=error_message)

@app.route('/add')
def add():
    return render_template('second1.html')

@app.route('/update')
def update():
    return render_template('second2.html')

@app.route('/delete')
def delete():
    return render_template('second3.html')

@app.route('/aggregates')
def aggregates():
    return render_template('second4.html')

@app.route('/select')
def select():
    return render_template('second5.html')

@app.route('/project')
def project():
    return render_template('second6.html')

@app.route('/search')
def search():
    return render_template('second7.html')

@app.route('/analytics')
def analytics():
    return render_template('second8.html')

@app.route('/exit')
def exit():
    return render_template('second9.html')

@app.route('/add_candidate')
def add_candidate():
    return render_template('second1a.html')

@app.route('/add_voter')
def add_voter():
    return render_template('second1b.html')

@app.route('/add_political_party')
def add_political_party():
    return render_template('second1c.html')

@app.route('/add_constituency')
def add_constituency():
    return render_template('second1d.html')

@app.route('/add_evm_machine')
def add_evm_machine():
    return render_template('second1e.html')

@app.route('/add_citizen')
def add_citizen():
    return render_template('second1f.html')


#TO INSERT CANDIDATE 1A
def insert_candidate(candidate_data):
    """
    Function to insert candidate data into the database
    """
    global db_connection
    if db_connection:
        try:
            with db_connection.cursor() as cur:
                query = """
                INSERT INTO Candidate 
                (candidate_id, name, aadhar_no, source_of_funding, total_donations, total_funding_received, total_expenditure, party_id, constituency_id)
                VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cur.execute(query, candidate_data)
                db_connection.commit()
                return("Candidate added!")
        except pymysql.Error as e:
            print("Error: ", e)
            return("Candidate not added!")
        




@app.route('/submit_candidate', methods=['POST'])
def submit_candidate():
    candidate_data = (
        request.form['candidate_id'],
        request.form['candidate_name'],
        request.form['aadhar_no'],
        request.form['source_of_funding'],
        request.form['total_donations'],
        request.form['total_funding_received'],
        request.form['total_expenditure'],
        request.form['party_id'],
        request.form['constituency_id']
    )

    ans = insert_candidate(candidate_data)
    return(ans)

#TO INSERT VOTER 1B
def insert_voter(voter_data):
    """
    Function to insert voter data into the database
    """
    global cursor, db_connection
    if db_connection:
        try:
            with db_connection.cursor() as cur:
                query = """
                INSERT INTO Voter 
                (aadhar_no, voter_id, dob, Street_address, gender, nationality, annual_income, Educational_Background, state, city, pincode,name, Voting_constituency)
                VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cur.execute(query, voter_data)
                db_connection.commit()
                return "Voter added successfully!"
        except pymysql.Error as e:
            print("Error: ", e)
            return "Voter not added!"
    else:
        return "Error: Database connection not established."

@app.route('/submit_voter', methods=['POST'])
def submit_voter():
    voter_data = (
        request.form['aadhar_no'],
        request.form['voter_id'],
        request.form['dob'],
        request.form['address'],
        request.form['gender'],
        request.form['nationality'],
        request.form['income'],
        request.form['education'],
        request.form['state'],
        request.form['city'],
        request.form['pincode'],
        request.form['voter_name'],
        request.form['constituency_id']
    )

    result = insert_voter(voter_data)
    return result

#TO INSERT POLITICAL PARTY 1C
def insert_political_party(political_party_data):
    """
    Function to insert political party data into the database
    """
    global cursor, db_connection
    if db_connection:
        try:
            with db_connection.cursor() as cur:
                query = """
                INSERT INTO Political_Party 
                (party_id, party_name, party_president,Party_Headquarters ,symbol, total_members, seats_contested)
                VALUES 
                (%s, %s, %s, %s, %s, %s, %s)
                """
                cur.execute(query, political_party_data)
                db_connection.commit()
                return "Political party added successfully!"
        except pymysql.Error as e:
            print("Error: ", e)
            return("Political party not added!")
    else:
        return("Error: Database connection not established.")

@app.route('/submit_party', methods=['POST'])
def submit_political_party():
    political_party_data = (
        request.form['party_id'],
        request.form['party_name'],
        request.form['president'],
        request.form['hq'],
        request.form['party_symbol'],
        request.form['total_members'],
        request.form['seats_contested']
    )

    result = insert_political_party(political_party_data)
    return result



# TO INSERT CONSTITUENCY 1D
def insert_constituency(constituency_data):
    """
    Function to insert constituency data into the database
    """
    global cursor, db_connection
    if db_connection:
        try:
            with db_connection.cursor() as cur:
                query = """
                INSERT INTO Constituency 
                (C_ID, C_Name, State_Name, Total_Residing_Citizens, Polling_Booths, EVM_Machines)
                VALUES 
                (%s, %s, %s, %s, %s, %s)
                """
                cur.execute(query, constituency_data)
                db_connection.commit()
                print("Constituency added successfully!")
        except pymysql.Error as e:
            print("Error: ", e)
            print("Constituency not added!")
    else:
        print("Error: Database connection not established.")


@app.route('/submit_constituency', methods=['POST'])
def submit_constituency():
    constituency_data = (
        request.form['constituency_id'],
        request.form['constituency_name'],
        request.form['state'],
        request.form['total_citizens'],
        request.form['total_polling_booths'],
        request.form['total_machines']
    )

    insert_constituency(constituency_data)
    return "Constituency added successfully!"

#TO INSERT EVM 1E
def insert_evm(evm_data):
    """
    Function to insert EVM data into the database
    """
    global cursor, db_connection
    if db_connection:
        try:
            with db_connection.cursor() as cur:
                query = """
                INSERT INTO EVM_Machine 
                (machine_id, No_of_Votes, Const_ID)
                VALUES 
                (%s, %s, %s)
                """
                cur.execute(query, evm_data)
                db_connection.commit()
                print("EVM added successfully!")
        except pymysql.Error as e:
            print("Error: ", e)
            print("EVM not added!")
    else:
        print("Error: Database connection not established.")


@app.route('/submit_machine', methods=['POST'])
def submit_evm():
    evm_data = (
        request.form['machine_id'],
        request.form['num_votes'],
        request.form['constituency_id']
    )

    insert_evm(evm_data)
    return "EVM added successfully!"


#TO INSERT CITIZEN 1F
def insert_citizen(citizen_data):
    """
    Function to insert citizen data into the database
    """
    global cursor, db_connection
    if db_connection:
        try:
            with db_connection.cursor() as cur:
                query = """
                INSERT INTO Citizen 
                (Citizen_ID, aadhar_no, name, dob, street_address, gender, nationality, annual_income, Educational_Background, state, city, pincode, Contact_Number, Email_Address)
                VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cur.execute(query, citizen_data)
                db_connection.commit()
                return "Citizen added successfully!"
        except pymysql.Error as e:
            print("Error: ", e)
            return "Citizen not added!"
    else:
        return "Error: Database connection not established."


@app.route('/submit_citizen', methods=['POST'])
def submit_citizen():
    citizen_data = (
        request.form['citizen_id'],
        request.form['aadhar_no'],
        request.form['citizen_name'],
        request.form['dob'],
        request.form['street_address'],
        request.form['gender'],
        request.form['nationality'],
        request.form['annual_income'],
        request.form['education'],
        request.form['state'],
        request.form['city'],
        request.form['pincode'],
        request.form['contact_no'],
        request.form['email']
    )

    result = insert_citizen(citizen_data)
    return result


#second2


@app.route('/update_can')
def update_candidate():
    # Logic to update candidate details in the database
    # Render the template for updating candidate details
    return render_template('second2a.html')

@app.route('/update_voter')
def update_voter():
    # Logic to update voter details in the database
    # Render the template for updating voter details
    return render_template('second2b.html')

@app.route('/update_party')
def update_party():
    # Logic to update political party details in the database
    # Render the template for updating political party details
    return render_template('second2c.html')

def gettype(attribute,table):
    global cursor, db_connection
    query = f"SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{table}' AND COLUMN_NAME = '{attribute}';"
    try:
        with db_connection.cursor() as cur:
            cur.execute(query)
            result = cur.fetchone()
            if result is None:
                return None
            else:
                return result['DATA_TYPE']
    except Exception as e:
        print("Error: ", e)
        return None


@app.route('/update_candidate_details', methods=['POST'])
def update_candidate_details():
    global db_connection
    if db_connection:
        try:
            candidate_id = request.form['candidate_id']
            with db_connection.cursor() as cur:
                query = f"SELECT * FROM Candidate WHERE candidate_id = {candidate_id};"
                cur.execute(query)
                result = cur.fetchone()
                if result is None:
                    return "Candidate not found!"
                else:
                    num_attributes = int(request.form['num_attributes'])
                    attribute_value_list = []
                    for i in range(num_attributes):
                        attribute_name = request.form[f'attribute_name_{i+1}']
                        value = request.form[f'attribute_value_{i+1}']
                        attribute_value_list.append((attribute_name, value))
                    print(attribute_value_list)
                    for attribute, value in attribute_value_list:
                        if 'char' in gettype(attribute, "Candidate"):
                            query = f"UPDATE Candidate SET {attribute} = %s WHERE candidate_id = %s;"
                            cur.execute(query, (value, candidate_id))
                        else:
                            query = f"UPDATE Candidate SET {attribute} = %s WHERE candidate_id = %s;"
                            cur.execute(query, (value, candidate_id))
                    
                    db_connection.commit()
                    return "Candidate details updated successfully!"
        except pymysql.Error as e:
            return f"Error: {e}"
    else:
        return "Error: Database connection not established."


# UPDATE 2b
@app.route('/update_voter_details', methods=['POST'])
def update_voter_details_route():
    global db_connection
    if request.method == 'POST':
        voter_id = request.form.get('voter_id')
        num_attributes = int(request.form.get('num_attributes'))
        attribute_list = []
        for i in range(num_attributes):
            attribute_name = request.form.get(f'attribute_name_{i+1}')
            value = request.form.get(f'attribute_value_{i+1}')
            attribute_list.append((attribute_name, value))

        if db_connection:
            try:
                with db_connection.cursor() as cur:
                    query = f"SELECT * FROM Voter WHERE voter_id = {voter_id};"
                    cur.execute(query)
                    result = cur.fetchone()
                    if result is None:
                        return "Voter not found!"
                    else:
                        for attribute, value in attribute_list:
                            if 'char' in gettype(attribute, "Voter"):
                                query = f"UPDATE Voter SET {attribute} = '{value}' WHERE voter_id = {voter_id};"
                            else:
                                query = f"UPDATE Voter SET {attribute} = {value} WHERE voter_id = {voter_id};"
                            cur.execute(query)
                        db_connection.commit()
                        return "Voter details updated successfully!"
            except Exception as e:
                return f"Error: {e}"
        else:
            return "Error: Database connection not established."

    # If the request method is not POST, return an error message
    return "Invalid request."

#UPDATE 2C
@app.route('/update_party_details', methods=['POST'])
def update_party_details():
    if request.method == 'POST':
        party_id = request.form.get('party_id')
        num_attributes = int(request.form.get('num_attributes'))
        attribute_list = []
        for i in range(num_attributes):
            attribute_name = request.form.get(f'attribute_name_{i+1}')
            value = request.form.get(f'attribute_value_{i+1}')
            attribute_list.append((attribute_name, value))

        if db_connection:
            try:
                with db_connection.cursor() as cur:
                    query = f"SELECT * FROM Political_Party WHERE party_id = {party_id};"
                    cur.execute(query)
                    result = cur.fetchone()
                    if result is None:
                        return "Political party not found!"
                    else:
                        for attribute, value in attribute_list:
                            if 'char' in gettype(attribute, "Political_Party"):
                                query = f"UPDATE Political_Party SET {attribute} = '{value}' WHERE party_id = {party_id};"
                            else:
                                query = f"UPDATE Political_Party SET {attribute} = {value} WHERE party_id = {party_id};"
                            cur.execute(query)
                        db_connection.commit()
                        return "Political party details updated successfully!"
            except Exception as e:
                return f"Error: {e}"
        else:
            return "Error: Database connection not established."

    # If the request method is not POST, return an error message
    return "Invalid request."



#DELETE 3 
@app.route('/delete_can')
def delete_candidate():
    # Logic to delete candidate entry
    # Render template or return response
    return render_template('second3a.html')
    

@app.route('/delete_voter')
def delete_voter():
    # Logic to delete voter entry
    # Render template or return response
    return render_template('second3b.html')

@app.route('/delete_party')
def delete_party():
    # Logic to delete political party entry
    # Render template or return response
    return render_template('second3c.html')

#DELETE 3A
@app.route('/delete_candidate_action', methods=['POST'])
def delete_candidate_action():
    global db_connection
    if db_connection:
        candidate_id = request.form.get('candidate_id')
        try:
            with db_connection.cursor() as cur:
                query = f"SELECT * FROM Candidate WHERE candidate_id = {candidate_id};"
                cur.execute(query)
                result = cur.fetchone()
                if result is None:
                    return "Candidate not found!"
                else:
                    query = f"DELETE FROM Candidate WHERE candidate_id = {candidate_id};"
                    cur.execute(query)
                    db_connection.commit()
                    return "Candidate deleted successfully!"
        except Exception as e:
            return f"Error: {e}"
    else:
        return "Error: Database connection not established."


#DELETE 3B
@app.route('/delete_voter_action', methods=['POST'])
def delete_voter_action():
    global db_connection
    if db_connection:
        voter_id = request.form.get('voter_id')
        try:
            with db_connection.cursor() as cur:
                query = f"SELECT * FROM Voter WHERE voter_id = {voter_id};"
                cur.execute(query)
                result = cur.fetchone()
                if result is None:
                    return "Voter not found!"
                else:
                    query = f"DELETE FROM Voter WHERE voter_id = {voter_id};"
                    cur.execute(query)
                    db_connection.commit()
                    return "Voter deleted successfully!"
        except Exception as e:
            return f"Error: {e}. Voter not deleted!"
    else:
        return "Error: Database connection not established."

#DELETE 3C
@app.route('/delete_party_action', methods=['POST'])
def delete_party_action():
    global db_connection
    if db_connection:
        party_id = request.form.get('party_id')
        try:
            with db_connection.cursor() as cur:
                query = f"SELECT * FROM Political_Party WHERE party_id = {party_id};"
                cur.execute(query)
                result = cur.fetchone()
                if result is None:
                    return "Political party not found!"
                else:
                    query = f"DELETE FROM Political_Party WHERE party_id = {party_id};"
                    cur.execute(query)
                    db_connection.commit()
                    return "Political party deleted successfully!"
        except Exception as e:
            return f"Error: {e}"
    else:
        return "Error: Database connection not established."


#4A
@app.route('/get_total_polling_booths')
def get_total_polling_booths_route():
    result = get_total_polling_booths()
    return render_template('second4a.html', result=result)

def get_total_polling_booths():
    global db_connection
    try:
        with db_connection.cursor() as cur:
            query = f"SELECT SUM(Polling_Booths) FROM Constituency;"
            cur.execute(query)
            resultt = cur.fetchone()
            if resultt is None:
                return "Constituency not found!"
            else:
                return str(resultt['SUM(Polling_Booths)'])
    except Exception as e:
        return f"Error: {str(e)}"

#4B
@app.route('/get_max_votes_in_constituency')
def get_max_votes_in_constituency():
    # Logic to get maximum number of votes registered goes here
    return render_template('second4b.html')

@app.route('/get_max_votes_result', methods=['POST'])
def get_max_votes_result():
    if request.method == 'POST':
        constituency_id = request.form['constituencyId']
        print(constituency_id)
        global db_connection
        try:
            with db_connection.cursor() as cur:
                query = f"SELECT MAX(total_votes) FROM (SELECT SUM(V.Vote_Count) as total_votes From Vote_Count_Machine_Party V LEFT JOIN EVM_Machine E On V.Machine_ID = E.Machine_ID WHERE E.Const_ID = {constituency_id} GROUP BY V.Political_Party_ID) alias;"
                cur.execute(query)
                result = cur.fetchall()
                if result is None:
                    print("Constituency not found!")
                    return
                else:
                    # print("Maximum number of votes: ", result['MAX(Votes)'])
                    print(result)
                    max_votes_result=result
        except Exception as e:
            print("Error: ", e)
            print("Invalid constituency id!")
            max_votes_result="Invalid constituency id!"
        return render_template('result.html', result=max_votes_result)  # Render a template with the updated result

#4C
@app.route('/get_least_resource_consuming_constituency')
def get_least_resource_consuming_constituency():
    global db_connection
    try:
        with db_connection.cursor() as cur:
            query = f"SELECT C_Name FROM Constituency WHERE Polling_Booths IN (SELECT MIN(Polling_Booths) FROM Constituency);"
            cur.execute(query)
            result = cur.fetchone()
            if result is None:
                return "Constituency not found!"
            else:
                return render_template('second4c.html', result=result['C_Name'])
    except Exception as e:
        return f"Error: {str(e)}"


#4D
@app.route('/get_average_votes_per_booth')
def get_average_votes_per_booth():
    # Logic to get average votes per polling booth goes here
    return render_template('second4d.html')

@app.route('/get_average_votes_per_booth_result', methods=['POST'])
def get_average_votes_per_booth_result():
    if request.method == 'POST':
        constituency_id = request.form['constituencyId']
        print(constituency_id)
        global db_connection
        try:
            with db_connection.cursor() as cur:
                query = f"SELECT AVG(No_of_votes) FROM EVM_Machine WHERE Const_ID = {constituency_id};"
                cur.execute(query)
                result = cur.fetchone()
                if result is None:
                    print("Constituency not found!")
                    return "Constituency not found!"
                else:
                    average_votes = result['AVG(No_of_votes)']
        except Exception as e:
            print("Error: ", e)
            print("Invalid constituency id!")
            return "Error: Invalid constituency id!"

        return render_template('result.html', result=average_votes)


#5A
@app.route('/get_citizens_details')
def get_citizens_details():
    # Logic to retrieve details of citizens whose Gender is Male
    # Implement your logic here
    try:
        with db_connection.cursor() as cur:
            query = "SELECT * FROM citizen WHERE Gender = 'M';"
            cur.execute(query)
            results = cur.fetchall()
            if not results:
                return "No citizens found"
            else:
                # Process the results here if needed
                return render_template('second5a.html',result=results)
    except Exception as e:
        return f"Error: {e}"
    


#5B
@app.route('/get_employee_details')
def get_employee_details():
    # Logic to get employee details goes here
    return render_template('second5b.html')

@app.route('/get_employee_details_result', methods=['POST'])
def get_employee_details_result():
    if request.method == 'POST':
        dept = request.form['Working_Department']
        print(dept)
        try:
            with db_connection.cursor() as cur:
                query = f"SELECT * FROM Employee WHERE Working_Department = '{dept}';"
                cur.execute(query)
                results = cur.fetchall()
                if not results:
                    return "No employees found"
                else:
                    return render_template('result3.html', employees=results)
        except Exception as e:
            return f"Error: {e}"


# 5C
@app.route('/get_evm_machine_details')
def get_evm_machine_details():
    # Render the form to input constituency ID
    return render_template('second5c.html')

@app.route('/get_evm_machine_details_result', methods=['POST'])
def get_evm_machine_details_result():
    print("in get evm machines === ")
    if request.method == 'POST':
        try:
            # Retrieve constituency ID from the form
            constituency_id = int(request.form['constituencyId'])
            with db_connection.cursor() as cur:
                query = f"SELECT * FROM EVM_Machine WHERE Const_ID = {constituency_id};"
                cur.execute(query)
                result4 = cur.fetchall(),
                if not result4:
                    return "EVM Machine not found!"
                else:
                    # Render the template with the retrieved EVM machine details
                    return render_template('result4.html', evm_machines=result4)
        except Exception as e:
            return f"Error: {e}"



#7A
@app.route('/get_citizens_letter', methods=['GET'])
def get_letter():
    return render_template("second7a.html")

@app.route('/get_citizens_letter_result', methods=['POST'])
def search_citizen_by_letter():
    if request.method == 'POST':
        letter = request.form['letter']
        print(letter)
        global db_connection
        try:
            with db_connection.cursor() as cur:
                query = f"""
                    SELECT *
                    FROM citizen
                    WHERE Name LIKE "{letter}%";
                """
                cur.execute(query)
                result7a = cur.fetchall()

                if not result7a:
                    print("No Citizen found")
                    return "No Citizen found"
                else:
                    print("Citizens are as follows:")
                    for result in result7a:
                        print(result)
                    return render_template('result7.html', results=result7a)
        except Exception as e:
            print("Error: ", e)
            print("Invalid query or database connection!")
            return "Invalid query or database connection!"


#7B
@app.route('/get_manifesto_keyword', methods=['GET'])
def get_manifesto():
    return render_template("second7b.html")

@app.route('/get_manifesto_keyword_result', methods=['POST'])
def search_manifesto_by_keyword():
    if request.method == 'POST':
        word = request.form['word']
        print(word)
        global db_connection
        try:
            with db_connection.cursor() as cur:
                query = f"""
                    SELECT *
                    FROM manifesto
                    WHERE Content LIKE "%{word}%";
                """
                cur.execute(query)
                results7b = cur.fetchall()

                if not results7b:
                    print("No Manifesto found")
                    return "No Manifesto found"
                else:
                    print("Manifesto is as follows:")
                    for result in results7b:
                        print(result)
                    return render_template('result7b.html', results=results7b)
        except Exception as e:
            print("Error: ", e)
            print("Invalid Word")
            return "Invalid Word"

#8a
@app.route('/get_percentage_turnout', methods=['GET'])
def get_percentage_turnout():
    # Code to retrieve percentage turnout in a given state
    return render_template("second8a.html")


@app.route('/get_percentage_turnout_result', methods=['GET'])
def get_percentage_turnout_result():
    state_name = request.args.get('stateName')
    try:
        with db_connection.cursor() as cur:
            query1 = f"SELECT count(Citizen_ID) FROM citizen WHERE State = '{state_name}' AND DOB <= '2006-05-01' AND Nationality= 'Indian';"
            cur.execute(query1)
            result1 = cur.fetchone()
            
            query2 = f"SELECT count(Voter_ID) FROM voter WHERE State = '{state_name}';"
            cur.execute(query2)
            result2 = cur.fetchone()

            if result1['count(Citizen_ID)'] == 0:
                return render_template('result8a.html', turnout_result="No citizen belonging to this state is present in the database")
            else:
                percentage_turnout = (result2['count(Voter_ID)'] / result1['count(Citizen_ID)']) * 100
                return render_template('result8a.html', turnout_result=f"{result2['count(Voter_ID)']} people came to vote in overall from that constituency and {percentage_turnout:.2f} is the percentage turnout.")
    except Exception as e:
        print("Error: ", e)
        return render_template('result8a.html', turnout_result="Invalid Word")





#8b
@app.route('/get_fav_party', methods=['GET'])
def get_fav_party():
    # Code to retrieve favorite political party in a given state
    return render_template("second8b.html")


@app.route('/get_fav_party_result', methods=['GET'])
def get_fav_party_result():
    state = request.args.get('stateName')
    print("Received state:", state)  # Debug statement
    try:
        with db_connection.cursor() as cur:
            query3 = f"SELECT Political_Party_ID FROM ((EVM_Machine JOIN Vote_Count_Machine_Party ON EVM_Machine.Machine_ID = Vote_Count_Machine_Party.Machine_ID) RIGHT JOIN Constituency ON Const_ID = C_ID)  where  State_Name = '{state}' GROUP BY Political_Party_ID ORDER BY sum(Vote_Count) DESC LIMIT 1;"
            print("Query 3:", query3)  # Debug statement
            cur.execute(query3)
            result3 = cur.fetchone()
            print("Result 3:", result3)  # Debug statement
            query4 = f"SELECT Party_Name FROM Political_Party WHERE Party_ID = {result3['Political_Party_ID']};"
            print("Query 4:", query4)  # Debug statement
            cur.execute(query4)
            result4 = cur.fetchone()
            print("Result 4:", result4)  # Debug statement

            fav_party = f"The most famous political party among the state {state} is {result4['Party_Name']}"
            return render_template('result8b.html', fav_party=fav_party)
    except Exception as e:
        print("Error: ", e)
        return "Invalid State"




if __name__ == '__main__':
    app.run(debug=True)
