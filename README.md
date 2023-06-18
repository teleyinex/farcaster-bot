# Farcaster bot

Welcome! This is just a simple farcaster bot that allows you to cast text messages using:

- Github Actions (using the cron feature, so you can cast every N minutes)
- Google Spreadsheets (so you can share it with your friends and team to add new casts that will be casted automagically)

## Requirements

Before you start, you will need two things:

- A Farcaster account
- A Google Service account

### Farcaster accounts

Getting one nowadays should be easier (ask me as I might have some invitations left). If you have one,
all you have to do is use your "secret words" (aka mnemonic) to authenticate and cast.

You might not be confortable using your personal account for this, so the best way is to get another invite
and create for yourself a new account if you want to try this bot.

Once you have the account, extract the mnemonic and save it in a .env file like this:

```
FARCASTER_MNEMONIC = "your words"
```

### Google Spreadsheet Service Account

Now, you need to create in your Google Cloud a service account for accessing programatically your Google Drive.

First, you will need to create a project. Go to console.cloud.google.com and proceed.

Once you have created the project, select it. Then, go to the IAM & Admin section, and there select the
Service Accounts section.

There you should see the option of creating a new service account. Name it. Once you have it, create an associated key. Choose JSON format.

Save the file that you have downloaded, and keep it safe. Then you will need to give permissions to your app to access the Google Sheets API.
Just go to the API & Services, and enable it. If you click in the Credentials section you should see your previous created credential.

Copy the email of your service account, as you will need to share your spreadsheet with that email as an editor.

#### Saving the JSON credentials as an encoded base64 string

We will store the JSON file as an encoded base64 string because we will be using Github Actions for running the script.

NOTE: JSON data is not handled well with Github Actions secrets, so the best solution I've found is that.

Once you have the JSON as a base64 string, just save it in your .env file like this:

```
GOOGLE_AUTH = base64string
```

#### Spreadsheet with your content

Now time to create the Spreadsheet that you will be sharing with your Service Account (and probably your friends).

Just go to Google and create one. It will need to have at least 2 sheets:

- First one named: dashboard
- Second one named: whatever you want (i.e casts).

The first one is really important because it is our index or dashboard. In the cell A1 you will have the latest
sheet used to cast a message. If you are following now the tutorial, you should write in your cell A1 casts (if you named
your second sheet 'casts').

Then, in the second sheet you can start adding casts as you want. The idea is each row is a cast.
You should be using only A column and write there your quotes, messages, whatever.

In order to get the script running you will need to add in the column B the following word: "last".
Why? Because that will instruct the script to know which was the last cast that has been casted, choosing the next one
and casting it (obviously, it will update the status of last to this last one).

You can have as many sheets as you want. The idea is that they could serve as topics for your casts:

- Support casts
- Quotes
- Nice things
- ...

The script will iterate over each sheet in a round robin fashion. This will enable you to have more topics, and your bot
will seem more interesting (or maybe not).

Now copy the URL of the file and save it in the .env file:

```
URL = 'your url'
```

### Installing libraries

Now that you have all setup, you need to install the libraries:

```
python -menv env
source env/bin/activate
pip install -r requirements.txt
```

NOTE: Use python 3.8 to 3.10. The Farcaster library doesn't support python 3.11.

You can now try to cast from your laptop:

```
python app.py
```

If you don't see any message, it means it worked! Go to your Farcaster account and check if you see the message.
If you see it, everything is ok and we can move into the next phase: casting automagically thanks to Github Actions.

### Setting up Github Actions

As you will see, this repo has a github action named "farcaster.yml". There you will see several repository secrets.

Those secrets should be created in the config section of the repository copying the values of your .env file.

Once you have it, adapt the timing (by default casts 4 times per day).

Enjoy!!!
