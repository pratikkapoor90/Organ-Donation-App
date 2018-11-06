#Load up the app
from organdonationwebapp import app, sc, ac, hc, uc, ruc, duc
# Launching server
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5555
    try:
        app.run(HOST, PORT, debug=True)
    except Exception as err:
        sc.closeDBConnection()
        print (err)
        print ("Something went wrong running the app")
    finally:
        sc.closeDBConnection()
        print ("Closing Database connection successfully")