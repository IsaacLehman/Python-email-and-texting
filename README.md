# Python-email-and-texting

    Python Messaging package using the built in SMTP library.
    Features:
        - Email
            - HTML
            - Plain Text
        - SMS
        - Sends through your Gmail account
            NOTE: gmail account must have 'Less Secure APP Access' enabled.
                  Set this in your acount security settings.

    Overview of provided message types:
        1. Email
            - to: example@example.com (String)
            - subject: (String)
            - body: (String) -> Can be in HTML format
            - is_HTML: defaults to False -> set True if body is in HTML format
        2. SMS
            - number: '12222222222' (String) -> include country code and area code
            - gateway: @txt.att.net (String) -> the SMS Gateway for the number
                - Look at the provider of recipient to select gateway
            - subject: (String)
            - body: (String)
            - recipient: DO NOT SET (auto created -> String)

    Overview of Messanger:
        - username: (String)
        - password: (String)
        Provided Functions: -> Example usage below
            - open_conn()
            - close_conn()
            - send_txt(msg, one_time=False)
            - send_email(msg, one_time=False)

    EXAMPLES:
    ----------------------------------------------------------------------------
    Example usage (one_time): -> cleaner code if sending one message

        my_messanger = Messanger(<your gmail username>, <your gmail password>)

        msg = SMS(number, gateway, subject, body)
        my_messanger.send_txt(msg, one_time=True)

        msg = Email(to, subject, body)
        my_messanger.send_email(msg, one_time=True)


    Example usage (not one_time): -> faster for sending lots of messages

        my_messanger = Messanger(<your gmail username>, <your gmail password>)
        my_messanger.open_conn()

        # send as many messages as you want here
        msg = SMS(number, gateway, subject, body)
        my_messanger.send_txt(msg)

        msg = Email(to, subject, body)
        my_messanger.send_email(msg)

        my_messanger.close_conn()


    SMS GATEWAYS
    ----------------------------------------------------------------------------
    AT&T: [number]@txt.att.net
    Sprint: [number]@messaging.sprintpcs.com or [number]@pm .sprint.com
    T-Mobile: [number]@tmomail.net
    Verizon: [number]@vtext.com
    Boost Mobile: [number]@myboostmobile.com
    Cricket: [number]@sms.mycricket.com
    Metro PCS: [number]@mymetropcs.com
    Tracfone: [number]@mmst5.tracfone.com
    U.S. Cellular: [number]@email.uscc.net
    Virgin Mobile: [number]@vmobl.com
