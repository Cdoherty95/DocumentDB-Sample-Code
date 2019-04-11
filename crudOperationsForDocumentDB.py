from pymongo import MongoClient

# Global variables to store information about the DocumentDB Cluster
DatabaseUserName = ''
DatabasePassword = ''
DatabaseEndpoint = ''

customerData = {
    "customer": [
        {
            "accountId": "5225167742487965",
            "SSN": "238402476",
            "firstName": "Michelle",
            "lastName": "Hannah",
            "gender": "female",
            "ethnicity": "white",
            "industry": "Food Preparation and Serving Related Occupations",
            "birthDate": {
                "month": "6",
                "day": "12",
                "year": "1964"
            },
            "address": [
                {
                    "status": "current",
                    "street": "3231 Joyce Street",
                    "city": "Ahoskie",
                    "state": "NC",
                    "zipCode": "27910"
                }
            ],
        },
        {
            "accountId": "4485519450034090",
            "SSN": "233308610",
            "firstName": "Peter",
            "lastName": "Fitzgibbon",
            "gender": "male",
            "ethnicity": "black",
            "industry": "Architecture and Engineering Occupations",
            "birthDate": {
                "month": "7",
                "day": "11",
                "year": "1976"
            },
            "address": [
                {
                    "status": "current",
                    "street": "4212 Hall Valley Drive",
                    "city": "Franklin",
                    "state": "WV",
                    "zipCode": "26807"
                }
            ],
        },
        {
            "accountId": "5153289148700175",
            "SSN": "354360474",
            "firstName": "Jean",
            "lastName": "Greenwood",
            "gender": "female",
            "ethnicity": "white",
            "industry": "Architecture and Engineering Occupations",
            "birthDate": {
                "month": "12",
                "day": "21",
                "year": "1966"
            },
            "address": [
                {
                    "status": "current",
                    "street": "2077 Oakmound Drive",
                    "city": "Chicago",
                    "state": "IL",
                    "zipCode": "60606"
                }
            ],
        },
        {
            "accountId": "4916896996552069",
            "SSN": "415617119",
            "firstName": "Mary",
            "lastName": "Bush",
            "gender": "female",
            "ethnicity": "asian",
            "industry": "Military Specific Occupations",
            "birthDate": {
                "month": "9",
                "day": "1",
                "year": "1999"
            },
            "address": [
                {
                    "status": "current",
                    "street": "82 Wilkinson Street",
                    "city": "Nashville",
                    "state": "TN",
                    "zipCode": "37201"
                }
            ],
        },
    ]
}

def connect_to_documentdb():
    # http://api.mongodb.com/python/2.7rc0/tutorial.html

    # MongoDB connection URI. Based off of aws console. we can use the ssl but
    # .pem file is only on ec2 so for testing Im not using it
    mongodb_uri = "mongodb://"+DatabaseUserName+":"+DatabasePassword+"@"+DatabaseEndpoint+":27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0"

    # This creates the connection to the MongoDB server in aws
    client = MongoClient(mongodb_uri)

    # MongoDB will create the database if it does not exist, and make a connection to it.
    # a database is not created until it gets content
    customer_db_connection = client["customer_information_db"]

    # Variable to specify collection in our db
    customer_db_collection = customer_db_connection["customers"]

    return customer_db_collection

# Inserting data into our documentdb database
def insert_into_db():

    # Variable to hold the connection to our db
    db_connection = connect_to_documentdb()

    # Insert each set of customer information as a document
    for customer in customerData['customer']:
        print(customer)
        returnFromInsert = db_connection.insert_one(customer)
        print(returnFromInsert)

insert_into_db()