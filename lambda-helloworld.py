def lambda_handler(event, context):
    # TODO implement
    print('my objects' +str(event.items()))
    return 'Hello from Lambda' +str(event.items())
    #return ('we recieved' +str(event.items()))
