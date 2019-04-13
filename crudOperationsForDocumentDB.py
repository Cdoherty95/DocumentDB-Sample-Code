# Written By Chris Doherty
# IIT ITMO 557 - Storage Technologies: Research Paper
# AWS DocumentDB: A NoSQL Document Database Service Provided by Amazon Web Services
# Python Version: 3.7.2
# This file will: insert customer data into a DocumentDB Cluster

# Import Statement
from pymongo import MongoClient

# Global variables to store information about the DocumentDB Cluster
DatabaseUserName = ''
DatabasePassword = ''
DatabaseEndpoint = ''

# Customer data to insert into DocumentDB. Each customer will be their own document
customerData = {
    "customer": [
        {
            "accountId": "5225167742487965",
            "SSN": "238402476",
            "firstName": "Michelle",
            "lastName": "Hannah",
            "gender": "female",
            "ethnicity": "White",
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
            "ethnicity": "Black",
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
            "ethnicity": "White",
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
            "ethnicity": "Asian",
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
        {
            "accountId": "4532839403993108",
            "SSN": "363565597",
            "firstName": "Mary",
            "lastName": "Blake",
            "gender": "female",
            "ethnicity": "White",
            "industry": "Office and Administrative Support Occupations",
            "birthDate": {
                "month": "5",
                "day": "19",
                "year": "1995"
            },
            "address": [
                {
                    "status": "current",
                    "street": "4183 Bombardier Way",
                    "city": "Southfield",
                    "state": "MI",
                    "zipCode": "48075"
                }
            ],
        },
    ]
}


# This function will return a connection to DocumentDB collection in a database
def connect_to_documentdb():
    # http://api.mongodb.com/python/2.7rc0/tutorial.html

    # MongoDB connection URI. Based off of AWS console.
    mongodb_uri = "mongodb://" + DatabaseUserName + ":" + DatabasePassword + "@" + DatabaseEndpoint + ":27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0"

    # This creates the connection to the MongoDB server in aws
    client = MongoClient(mongodb_uri)

    # MongoDB will create the database if it does not exist, and make a connection to it.
    # a database is not created until it gets content
    customer_db_connection = client["customer_information_db"]

    # Variable to specify collection in our db
    customer_db_collection = customer_db_connection["customers"]

    # Return connection to DocumentDB Collection
    return customer_db_collection


# Function to insert data into a DocumentDB database
def insert_into_db():
    # Variable to hold the connection to our db
    db_connection = connect_to_documentdb()

    # Insert each set of customer information as a document
    for customer in customerData['customer']:
        # Call to insert one customer into the collection
        return_from_insert_statement = db_connection.insert_one(customer)

        # Print out response from inserting data
        print(return_from_insert_statement)


# Call to insert data into the database
insert_into_db()
