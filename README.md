# CubingAtHomeBot
CubingAtHomeBot is an application created to run the second Cubing At Home competition. It is currently being hosted at https://cubething.kikoho.xyz. If you have any questions you can contact tyler.geist1111@gmail.com.
<br><br>
## Running a Competition
All you need to create a competition is a google sheet with certain formatting. You can get the formatting here: https://docs.google.com/spreadsheets/d/1YWisYkk5w2AojH4IQtcmehZkFAzlgTpVUdkwtqdyb-Y/copy.
<br>
### Create Event
Once replacing all the placeholder data you will have to share the sheet with the service account <b>cubingbot@cubingbot-279013.iam.gserviceaccount.com</b>. You can then go to https://cubething.kikoho.xyz/url and put in the link to the google sheets module from your address bar and the name sheet where your events are stored. This will create the link you will give to your competitors that references back to that module and sheet.
### Seeing Reults
When times have been submitted they will be put into a sheet with the same name as the event. The times will noted in terms of seconds and sorted by time entered. 
### Formatting Times
When all times have been submitted for an event you can then format the times to a more readable format. Using https://cubething.kikoho.xyz/format, put the link to the sheet and the name of the event in the website. When you submit and new sheet will be created that is the name of your event + (r)(ex: 3x3 R1(r)). This sheet will be sorted by best time and have the average and place displayed.
<br>
## Information
This tool was created using Python and vanilla HTML, Javascript and CSS.
## License
MIT  © Tyler Geist
