def lambda_handler(event, context):

    customer_id = event.get("customer_id")

    if customer_id is None:
        raise Exception("Invalid payload")

    return {
        "statusCode": 200
    }