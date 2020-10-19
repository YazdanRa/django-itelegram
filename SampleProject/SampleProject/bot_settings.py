DJANGO_TELEGRAMBOT = {
    "DISABLE_SETUP": False,
    #
    # TODO: Explain more about this key
    "MODE": "POLLING",  # (Optional [str])
    #
    # The default value is WEBHOOK, otherwise you may use "POLLING"
    # NB: if use polling mode you must provide to run a management command that starts a worker
    "WEBHOOK_SITE": "https://mywebsite.com",  # Required on WEBHOOK mode
    #
    # TODO: Explain more
    "WEBHOOK_PREFIX": "/prefix",  # (Optional[str])
    #
    # If this value is specified, a prefix is added to webhook url
    # "WEBHOOK_CERTIFICATE" : "cert.pem",
    # If your site use self-signed certificate, must be set with location of your public key
    # certificate.(More info at https://core.telegram.org/bots/self-signed )
    "STRICT_INIT": True,  # Optional[bool]
    #
    # TODO: Explain more about this key
    "BOTS": [
        {
            "ID": "MyBot",  # (Optional[str])
            #
            # You can use this ID to get your bot in all the installed apps
            "TOKEN": "1062412615:AAHLZ974OBY3goSSoX6HePTapjgdJMYFnEY",  # (Required[str])
            #
            # Your bot token.
            # you can get it from ( https://t.me/BotFather )
            "CONTEXT": True,
            #
            # TODO: Explain more about this key
            # "ALLOWED_UPDATES": [],  # (Optional[list[str]])
            #
            # List the types of updates you want your bot to receive.
            # For example, specify ``["message", "edited_channel_post", "callback_query"]``
            # to only receive updates of these types.
            # See ``telegram.Update`` for a complete list of available update types.
            # Specify an empty list to receive all updates regardless of type (default).
            # If not specified, the previous setting will be used.
            # Please note that this parameter doesn't affect updates created before the call to the setWebhook,
            # so unwanted updates may be received for a short period of time.
            # "TIMEOUT": 60,  # (Optional[int|float])
            #
            # If this value is specified, use it as the read timeout from the server
            # "WEBHOOK_MAX_CONNECTIONS": 40,  # (Optional[int])
            #
            # Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100.
            # Defaults to 40. Use lower values to limit the load on your bot's server,
            # and higher values to increase your bot's throughput.
            # "POLL_INTERVAL": 0.0,  # (Optional[float])
            #
            # Time to wait between polling updates from Telegram in seconds.
            # Default is 0.0
            # "POLL_CLEAN": False,  # (Optional[bool])
            #
            # Whether to clean any pending updates on Telegram servers before actually starting to poll.
            # Default is False.
            # "POLL_BOOTSTRAP_RETRIES": 0,  # (Optional[int])
            #
            # Whether the bootstrapping phase of the `Updater`
            # will retry on failures on the Telegram server.
            # |   < 0 - retry indefinitely
            # |     0 - no retries (default)
            # |   > 0 - retry up to X times
            # "POLL_READ_LATENCY": 2,  # (Optional[float|int])
            #
            # Grace time in seconds for receiving the reply from server.
            # Will be added to the `timeout` value and used as the read timeout from server.
            # Default is 2
            # "PROXY": {}, # (Optional[dict]),
            #
            # Use proxy to communicate with Telegram API server. Example:
            #    {
            #        "proxy_url": "socks5://ip:port",
            #        "urllib3_proxy_kwargs": {
            #             "username": "username",
            #             "password": "password"
            #        }
            #    }
            # Default is not to use any proxy.
        },
        # Other bots here with same structure.
    ],
}
