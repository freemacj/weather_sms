# Wunderground API

Note: I have recently updated the Wunderground API code sample provided for python to ensure this code runs for python 3. If forking this repo, all that needs to be added to this script is your personal API key into a seperate file in the same directory titled config.py like this:

    ```   
    api_key = "your_api_key_here"
    ```

Instuctions to obtain your personal API key are found below:

Getting Started

Before you start using the Weather API, it is important to know that

1. Most of the API features require an API key. [Sign up for a key.](https://www.wunderground.com/weather/api/d/docs?d=data/index)
2. [API requests](https://www.wunderground.com/weather/api/d/docs?d=data/index) are made over HTTP. Data features return JSON or XML. WunderMap layer features return image files. This documentation is full of examples of how to use API features. [See code samples for several languages](https://www.wunderground.com/weather/api/d/docs?d=resources/code-samples) and [user-generated code and libraries](https://www.wunderground.com/weather/api/d/docs?d=resources/user-generated-code).
3. Multiple API features can be combined into a single HTTP request. This is an easy way to economize your requests. The [Data Features](https://www.wunderground.com/weather/api/d/docs?d=data/index) page documents how features can be combined into a single request.
4. Per the [Terms of Service](https://www.wunderground.com/weather/api/d/terms.html) the Weather Underground logo must be included with a credit line where Weather Underground data is displayed. Please see individual Logo variations for all acceptable combinations of layout in the [Logo Usage Guide](https://www.wunderground.com/weather/api/d/docs?d=resources/logo-usage-guide).
