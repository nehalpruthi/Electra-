import subprocess as sp
import pymysql
import pymysql.cursors


def gettype(attribute,table):
    query = f"SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{table}' AND COLUMN_NAME = '{attribute}';"
    try:
        with con.cursor() as cur:
            cur.execute(query)
            result = cur.fetchone()
            if result is None:
                return None
            else:
                return result['DATA_TYPE']
    except Exception as e:
        print("Error: ", e)
        return None

def option1():
    """
    Function to implement option 1
    """
    tmp = sp.call('clear', shell=True)
    print("Enter your choice:")
    print("1. Add a new candidate")
    print("2. Add a new voter")
    print("3. Add a new political party")
    print("4. Add a new constituency")
    print("5. Add a new EVM machine")
    print("6. Add a new citizen")
    ch = int(input("Enter choice> "))

    if ch == 1:
        print("Enter candidate details:")
        candidate_id = int(input("Enter candidate id: "))
        name = input("Enter candidate name: ")
        aadhar_no = int(input("Enter candidate aadhar no: "))
        source_of_funding = input("Enter candidate source of funding: ")
        total_donations = int(input("Enter candidate total donations: "))
        total_funding_received = int(input("Enter candidate total funding received: "))
        total_expenditure = int(input("Enter candidate total expenditure: "))
        party_id = int(input("Enter candidate party id: "))
        constituency_id = (input("Enter candidate constituency id: "))
        
        
        try:
            with con.cursor() as cur:
                # print("hi")
                query = f"INSERT INTO Candidate VALUES ({candidate_id}, '{name}', {aadhar_no}, '{source_of_funding}', {total_donations}, {total_funding_received}, {total_expenditure}, {party_id}, '{constituency_id}');"
                print(query)
                cur.execute(query)
                con.commit()
                print("Candidate added successfully!")
        except Exception as e:
            print("Error: ", e)
            print("Candidate not added!")

    elif ch == 2:
        print("Enter voter details:")
        aadhar_no = int(input("Enter voter aadhar no: "))
        voter_id = int(input("Enter voter id: "))
        dob = input("Enter voter date of birth (YYYY-MM-DD): ")
        street_address = input("Enter voter street address: ")
        gender = input("Enter gender(M/F): ")
        nationality = input("Enter nationality")
        annual_income = int(input("Enter annual income: "))
        education = input("Enter education: ")
        state = input("Enter state: ")
        city = input("Enter city: ")
        pincode = int(input("Enter pincode: "))

        name = input("Enter voter name: ")
        constituency = input("Enter voter constituency id: ")
        
        try:
            with con.cursor() as cur:
                query = f"INSERT INTO voter VALUES ({aadhar_no}, {voter_id}, '{dob}', '{street_address}','{gender}','{nationality}',{annual_income},'{education}','{state}','{city}',{pincode},'{name}','{constituency}');"
                cur.execute(query)
                con.commit()
                print("Voter added successfully!")
        except Exception as e:
            print("Error: ", e)
            print("Voter not added!")

    elif ch == 3:
        print("Enter political party details:")
        party_id = int(input("Enter party id: "))
        name = input("Enter party name: ")
        president = input("Enter president")
        hq = input("Enter hq")
        symbol = input("Enter party symbol: ")
        tot_members = int(input("Enter total members: "))
        seats_contested = int(input("Enter seats contested: "))

        
        try:
            with con.cursor() as cur:
                query = f"INSERT INTO Political_Party VALUES ({party_id}, '{name}', '{president}', '{hq}','{symbol}',{tot_members},{seats_contested});"
                cur.execute(query)
                con.commit()
                print("Political party added successfully!")
        except Exception as e:
            print("Error: ", e)
            print("Political party not added!")

    elif ch == 4:


        constituency_id = int(input("Enter constituency id: "))
        name = input("Enter constituency name: ")
        state = input("Enter state: ")
        total_city = int(input("Enter total citizens: "))
        poll_booth = int(input("Enter total polling booths: "))
        tot_machine = int(input("Enter total machines: "))

        try:
            with con.cursor() as cur:
                query = f"INSERT INTO Constituency VALUES ({constituency_id}, '{name}', '{state}', {total_city},{poll_booth},{tot_machine});"
                cur.execute(query)
                con.commit()
                print("Constituency added successfully!")
        except Exception as e:
            print("Error: ", e)
            print("Constituency not added!")

    elif ch == 5:

        mach_id = int(input("Enter machine id: "))
        no_of_votes = int(input("Enter number of votes: "))
        constituency_id = int(input("Enter constituency id: "))

        try:
            with con.cursor() as cur:
                query = f"INSERT INTO EVM_Machine VALUES ({mach_id}, {no_of_votes}, {constituency_id});"
                #print(query)
                cur.execute(query)
                con.commit()
                print("EVM added successfully!")
        except Exception as e:
            print("Error: ", e)
            print("EVM not added!")


    elif ch == 6:
        print("Enter citizen detals:")
        citizen_id = int(input("Enter citizen id: "))
        aadhar_no = int(input("Enter citizen aadhar no: "))
        name = input("Enter citizen name: ")
        dob = input("Enter citizen date of birth (YYYY-MM-DD): ")
        street_address = input("Enter citizen street address: ")
        gender = input("Enter Gender(M/F):")
        nationality = input("Enter Nationality")
        annual_income = int(input("Enter annual income: "))
        education = input("Enter education: ")
        state = input("Enter state: ")
        city = input("Enter city: ")
        pincode = int(input("Enter pincode: ")) 
        contact_no = int(input("Enter contact no: "))
        email = input("Enter email: ")

        try:
            with con.cursor() as cur:
    
                sql_query = f"INSERT INTO citizen VALUES({citizen_id}, {aadhar_no}, '{name}', '{dob}', '{street_address}', '{gender}', '{nationality}', {annual_income}, '{education}', '{state}', '{city}', {pincode}, {contact_no}, '{email}');"
                cur.execute(sql_query)
                con.commit()
                print("Citizen added successfully!")

        except Exception as e:
                print("Error: ", e)
                print("Citizen not added!")



    else:
        print("Error: Invalid choice")

def option2():
    """
    Function to implement option 1
    """
    tmp = sp.call('clear', shell=True)

    print("Enter your choice:")
    print("1. Update candidate details")
    print("2. Update voter details")
    print("3. Update political party details")
    ch = int(input("Enter choice> "))

    if ch == 1:
        candidate_id = int(input("Enter candidate id: "))
        
        with con.cursor() as cur:
            query = f"SELECT * FROM Candidate WHERE candidate_id = {candidate_id};"
            cur.execute(query)
            result = cur.fetchone()
            if result is None:
                print("Candidate not found!")
                return
            else:
                
                # print("Enter number of attributes to be updated:")
                n = int(input("Enter number of attributes: "))
                list = []
                print(n)
                print("Enter attribute_name and new value:")
                for i in range(n):
                    attribute_name= input("Enter attribute name: ")
                    value=input("Enter Value: ")
                    list.append((attribute_name,value))
                print(list)
                
                for i in range(n):
                    
                    try:
                        with con.cursor() as cur:
                            if('char' in gettype(list[i][0],"Candidate")):
                                query = f"UPDATE Candidate SET {list[i][0]} = '{list[i][1]}' WHERE candidate_id = {candidate_id};"
                            else:
                                query = f"UPDATE Candidate SET {list[i][0]} = {list[i][1]} WHERE candidate_id = {candidate_id};"
                            cur.execute(query)
                            con.commit()
                    except Exception as e:
                        print("Error: ", e)
                        print("Invalid attribute/value not updated!")
                    
                print("Candidate updated successfully!")
    elif ch == 2:
        print("Enter voter_id of voter to be updated:")
        voter_id = int(input("Enter voter id: "))

        with con.cursor() as cur:
            query = f"SELECT * FROM Voter WHERE voter_id = {voter_id};"
            cur.execute(query)
            result = cur.fetchone()
            if result is None:
                print("Voter not found!")
                return
            else:
                
                # print("Enter number of attributes to be updated:")
                n = int(input("Enter number of attributes: "))
                list = []
                print("Enter attribute name and value: ")
                for i in range(n):
                    attribute_name= input("Enter attribute name: ")
                    value=input("Enter Value: ")
                    # print("Enter attribute_name and new value:")
                    list.append((attribute_name,value))
                
                for i in range(n):
                    
                    try:
                        with con.cursor() as cur:
                            if('char' in gettype(list[i][0],"voter")):
                                query = f"UPDATE Voter SET {list[i][0]} = '{list[i][1]}' WHERE voter_id = {voter_id};"
                            else:
                                query = f"UPDATE voter SET {list[i][0]} = {list[i][1]} WHERE voter_id = {voter_id};"
                            cur.execute(query)
                            con.commit()

                    except Exception as e:
                        print("Error: ", e)
                        print("Invalid attribute/value not updated!")
                        return
                print("Voter updated successfully!")

    elif ch == 3:

        print("Enter party_id of political party to be updated:")
        party_id = int(input("Enter party id: "))
        
        with con.cursor() as cur:
            query = f"SELECT * FROM Political_Party WHERE party_id = {party_id};"
            cur.execute(query)
            result = cur.fetchone()
            if result is None:
                print("Political party not found!")
                return
            else:
                
                # print("Enter number of attributes to be updated:")
                n = int(input("Enter number of attributes: "))
                list = []
                for i in range(n):
                    # print("Enter attribute_name and new value:")
                    attribute_name= input("Enter attribute name: ")
                    value=input("Enter Value: ")
                    list.append((attribute_name,value))
                
                for i in range(n):
                    
                    try:
                        with con.cursor() as cur:
                            if('char' in gettype(list[i][0],"Political_Party")):
                                query = f"UPDATE Political_Party SET {list[i][0]} = '{list[i][1]}' WHERE party_id = {party_id};"
                            else:
                                query = f"UPDATE Political_Party SET {list[i][0]} = {list[i][1]} WHERE party_id = {party_id};"
                            cur.execute(query)
                            con.commit()
                    except Exception as e:
                        print("Error: ", e)
                        print("Invalid attribute/value not updated!")
    
                print("Political party updated successfully!")
    else:
        print("Error: Invalid choice")


def option3():
    """
    Function to implement option 2
    """
    tmp = sp.call('clear', shell=True)

    print("Enter your choice:")
    print("1. Delete a candidate")
    print("2. Delete a voter")
    print("3. Delete a political party")
    ch = int(input("Enter choice> "))

    if ch == 1:
        print("Enter candidate_id of candidate to be deleted:")
        candidate_id = int(input("Enter candidate id: "))
        
        with con.cursor() as cur:
            query = f"SELECT * FROM Candidate WHERE candidate_id = {candidate_id};"
            cur.execute(query)
            result = cur.fetchone()
            if result is None:
                print("Candidate not found!")
                return
            else:
                
                try:
                    with con.cursor() as cur:
                        query = f"DELETE FROM Candidate WHERE candidate_id = {candidate_id};"
                        cur.execute(query)
                        con.commit()
                        print("Candidate deleted successfully!")
                except Exception as e:
                    print("Error: ", e)
                    print("Candidate not deleted!")
                    
    elif ch == 2:
        print("Enter voter_id of voter to be deleted:")
        voter_id = int(input("Enter voter id: "))
        
        with con.cursor() as cur:
            query = f"SELECT * FROM Voter WHERE voter_id = {voter_id};"
            cur.execute(query)
            result = cur.fetchone()
            if result is None:
                print("Voter not found!")
                return
            else:
                
                try:
                    with con.cursor() as cur:
                        query = f"DELETE FROM Voter WHERE voter_id = {voter_id};"
                        cur.execute(query)
                        con.commit()
                        print("Voter deleted successfully!")
                except Exception as e:
                    print("Error: ", e)
                    print("Voter not deleted!")

    elif ch == 3:

        print("Enter party_id of political party to be deleted:")
        party_id = int(input("Enter party id: "))
        
        with con.cursor() as cur:
            query = f"SELECT * FROM Political_Party WHERE party_id = {party_id};"
            cur.execute(query)
            result = cur.fetchone()
            if result is None:
                print("Political party not found!")
                return
            else:
                
                try:
                    with con.cursor() as cur:
                        query = f"DELETE FROM Political_Party WHERE party_id = {party_id};"
                        cur.execute(query)
                        con.commit()
                        print("Political party deleted successfully!")
                except Exception as e:
                    print("Error: ", e)
                    print("Political party not deleted!")


def option4():
    """
    Function to implement option 3
    """
    tmp = sp.call('clear',shell=True)

    print("Enter your choice:")
    print("1. Get total number of polling booth available for election")
    print("2. Get maximum number of votes registered by a party in a constituency")
    print("3. Get constituency which consumes least amount of resources")
    print("4. Get average votes per polling booth in a constituency")

    ch = int(input("Enter choice> "))
    if ch == 1:
        try:
            with con.cursor() as cur:
                query = f"SELECT SUM(Polling_Booths) FROM Constituency;"
                cur.execute(query)
                result = cur.fetchone()
                if result is None:
                    print("Constituency not found!")
                    return
                else:
                    print("Total number of polling booths: ", result['SUM(Polling_Booths)'])
        except Exception as e:
            print("Error: ", e)
            print("Invalid constituency id!")
    
    elif ch == 2:
        constituency_id = int(input("Enter constituency id: "))
        try:
            with con.cursor() as cur:
                query = f"SELECT MAX(total_votes) FROM (SELECT SUM(V.Vote_Count) as total_votes From Vote_Count_Machine_Party V LEFT JOIN EVM_Machine E On V.Machine_ID = E.Machine_ID WHERE E.Const_ID = {constituency_id} GROUP BY V.Political_Party_ID) alias;"
                cur.execute(query)
                result = cur.fetchall()
                if result is None:
                    print("Constituency not found!")
                    return
                else:
                    # print("Maximum number of votes: ", result['MAX(Votes)'])
                    print(result)
        except Exception as e:
            print("Error: ", e)
            print("Invalid constituency id!")

    elif ch == 3:
        query = f"Select C_Name from Constituency where Polling_Booths in (Select MIN(Polling_Booths) from Constituency);"
        try:
            with con.cursor() as cur:
                cur.execute(query)
                result = cur.fetchone()
                #print(result)
                if result is None:
                    print("Constituency not found!")
                    return
                else:
                    print(result['C_Name'])
        except Exception as e:
            print("Error: ", e)
            print("Invalid constituency id!")
    elif ch == 4:
        constituency_id = int(input("Enter constituency id: "))
        try:
            with con.cursor() as cur:
                query = f"SELECT AVG(No_of_votes) FROM EVM_Machine WHERE Const_ID = {constituency_id};"
                cur.execute(query)
                result = cur.fetchone()
                #print(result)
                if result is None:
                    print("Constituency not found!")
                    return
                else:
                    print("Average votes per polling booth: ", result['AVG(No_of_votes)'])
        except Exception as e:
            print("Error: ", e)
            print("Invalid constituency id!")

def option5():
    tmp = sp.call('clear',shell=True)
    print("Enter your choice:")
    print("1. Listing all details of citizens whose Gender is Male")
    print("2. Listing all the details of an employee who works in some department of Election Commission")
    print("3. Listing all the EVM_Machines of a particular constituency")

    ch = int(input("Enter choice> "))
    if(ch==1):
        try:
            with con.cursor() as cur:
                query = f"SELECT * FROM citizen WHERE Gender='M';"
                cur.execute(query)
                results = cur.fetchall()
                if not results:
                    print("No citizens found")
                else:
                    print("No such citizens")
        except Exception as e:
            print("Error: ", e)
    elif (ch==2):
        dept = (input("Enter Department of Election Commission: "))
        try:
            with con.cursor() as cur:
                query = f"SELECT * FROM Employee WHERE Working_Department='{dept}';"
                cur.execute(query)
                results = cur.fetchall()
                if not results:
                    print("No employees found")
                else:
                    print("Employees with given department")
                    for result in results:
                        print(result)
        except Exception as e:
            print("Error: ", e)
            print("Invalid Department")

    elif (ch==3):
        constituency_id = int(input("Enter constituency id: "))
        try:
            with con.cursor() as cur:
                query = f"SELECT * FROM EVM_Machine WHERE Const_id = {constituency_id};"
                cur.execute(query)
                results = cur.fetchall()
                if len(results)==0:
                    print("EVM Machine not found!")
                    return
                else:
                    print("EVM Machine with given Constituency")
                    for result in results:
                        print(result)
        except Exception as e:
            print("Error: ", e)
            print("Invalid constituency id!")

def option6():
    tmp = sp.call('clear',shell=True)
    print("Enter your choice:")
    print("1. Listing Names of all Members of Parliament of a Particular Party")
    print("2. Listing all the Responsibilities of a Department")
    print("3. Listing the Number of Members of a Particular Party")
    ch = int(input("Enter choice> "))
    
    if (ch==1):
        party_id=int(input("Enter Party id: "))
        try:
            with con.cursor() as cur:
                query = f"""
                    SELECT Candidate.Name
                    FROM Candidate
                    JOIN Member_of_Parliament ON Candidate.Candidate_ID = Member_of_Parliament.Cnd_ID
                    WHERE Member_of_Parliament.PP_ID = {party_id};
                """
                cur.execute(query)
                results = cur.fetchall()

                if not results:
                    print("No Members of Parliament for this Party ID")
                else:
                    print("Candidates from the specified party:")
                    for result in results:
                        print(result['Name'])
        except Exception as e:
            print("Error: ", e)
            print("Invalid Party_ID")
    elif (ch==2):
        department_id=int(input("Enter Department ID: "))
        try:
            with con.cursor() as cur:
                query = f"""
                    SELECT Responsibility from department_responsibility where D_ID={department_id};
                """
                cur.execute(query)
                results = cur.fetchall()

                if not results:
                    print("No Responsibity found ")
                else:
                    print("Responsibility for given department is :")
                    for result in results:
                        print(result['Responsibility'])
        except Exception as e:
            print("Error: ", e)
            print("Invalid Department ID")
    elif (ch==3):
        party_id=int(input("Enter Party id: "))
        try:
            with con.cursor() as cur:
                query = f"""
                    SELECT Total_Members
                    FROM Political_Party
                    WHERE Party_ID = {party_id};
                """
                cur.execute(query)
                results = cur.fetchall()

                if not results:
                    print("No Party found")
                else:
                    print("Total Members from the specified party:")
                    for result in results:
                        print(result['Total_Members'])
        except Exception as e:
            print("Error: ", e)
            print("Invalid Party_ID")

def option7():
    tmp = sp.call('clear',shell=True)
    print("Enter your choice:")
    print("1. Listing all details of citizens whose Name starts with a letter : ")
    print("2. Listing all the details of manifesto which has a Particular Keyword in its Content")
    ch = int(input("Enter choice> "))
    if(ch==1):
        letter=str(input("Enter Letter from which name should start"))
        try:
            with con.cursor() as cur:
                query = f"""
                    SELECT *
                    FROM citizen
                    WHERE Name LIKE "{letter}%";
                """
                cur.execute(query)
                results = cur.fetchall()

                if not results:
                    print("No Citizen found")
                else:
                    print("Citizen are as follows:")
                    for result in results:
                        print(result)
        except Exception as e:
            print("Error: ", e)
            print("Invalid Citizen")
    elif(ch==2):
        word=str(input("Enter Keyword in its content: "))
        try:
            with con.cursor() as cur:
                query = f"""
                    SELECT *
                    FROM manifesto
                    WHERE Content LIKE "%{word}%";
                """
                cur.execute(query)
                results = cur.fetchall()

                if not results:
                    print("No Manifesto found")
                else:
                    print("Manifesto is as follows:")
                    for result in results:
                        print(result)
        except Exception as e:
            print("Error: ", e)
            print("Invalid Word")



def option8():
    tmp = sp.call('clear',shell=True)
    print("Enter your choice:")
    print("1. Percentage turnout in a given state")
    print("2. Favourite Political Party in a given State")
    ch = int(input("Enter choice> "))

    if(ch==1):
        state = input("Enter the name of state:")
        try:
            with con.cursor() as cur:

                query1 = f"SELECT count(Citizen_ID) FROM citizen WHERE State = '{state}' AND DOB <= '2006-05-01' AND Nationality= 'Indian';"
                cur.execute(query1)
                result1 = cur.fetchone()
                print(result1)
                query2 = f"SELECT count(Voter_ID) FROM voter WHERE State = '{state}';"
                cur.execute(query2)
                result2 = cur.fetchone()
                print(result2)

                if result1==0 :
                    print("No citizen belonging to this state is present in the database")
                else :
                    percen = (result2['count(Voter_ID)']/result1['count(Citizen_ID)'])*100
                    print(f"{result2['count(Voter_ID)']} people came to vote in overall from that constituency and {percen} is the percentage turnout.")
        except Exception as e:
            print("Error: ", e)
            print("Invalid Word")
    elif (ch==2):
        state = input("Enter the name of the STATE: ")
        try:
            with con.cursor() as cur:
                query3 = f"SELECT Political_Party_ID FROM ((EVM_Machine JOIN Vote_Count_Machine_Party ON EVM_Machine.Machine_ID = Vote_Count_Machine_Party.Machine_ID) RIGHT JOIN Constituency ON Const_ID = C_ID)  where  State_Name = '{state}' GROUP BY Political_Party_ID ORDER BY sum(Vote_Count) DESC LIMIT 1;"
                cur.execute(query3)
                result3 = cur.fetchone()
                query4 = f"SELECT Party_Name FROM Political_Party WHERE Party_ID = {result3['Political_Party_ID']};"
                cur.execute(query4)
                result4 = cur.fetchone()

                print(f"The most famous political party among the state {state} is {result4['Party_Name']}")
        except Exception as e:
            print("Error: ", e)
            print("Invalid State")





def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        option1()
    elif(ch == 2):
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    elif(ch == 5):
        option5()
    elif(ch == 6):
        option6()
    elif(ch == 7):
        option7()
    elif(ch ==8):
        option8()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")
        try:
            with con.cursor() as cur:
                query = f"""
                    USE ELECTION;
                """
                cur.execute(query)
        except Exception as e:
            print("Error: ", e)
        

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Add a new candidate/voter/political party in the database:")  # Promote Employee
                print("2. Update database entries:")
                print("3. Delete a candidate/voter/political party from the database:")
                print("4. Get election aggregates:")
                print("5. Select data entities and retrieve their records:")
                print("6. Project data from the database:")
                print("7. Search the database:")
                print("8. Get data analytics:")
                print("9. Exit")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 9:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")