from string import Template

oauth_template = Template(
    """
    {
       "access_token":"${access_token}",
       "client_id":"${699175412021-g4523ttd4hbph0dmcqhsjjbu1l4htano.apps.googleusercontent.com}",
       "client_secret":"${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}",
       "refresh_token":"${refresh_token}",
       "token_expiry":"2020-10-27T18:03:48Z",
       "token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs"",
       "user_agent":null,
       "revoke_uri":"https://oauth2.googleapis.com/revoke",
       "id_token":null,
       "id_token_jwt":null,
       "token_response":{
          "access_token":"${refresh_token}",
          "expires_in": 3599,
          "scope":"https://www.googleapis.com/auth/youtube.upload",
          "token_type":"Bearer"
       },
       "scopes":[
          "https://www.googleapis.com/auth/youtube.upload"
       ],
       "token_info_uri":"https://oauth2.googleapis.com/tokeninfo",
       "invalid":false,
       "_class":"OAuth2Credentials",
       "_module":"oauth2client.client"
    }
            """

)
