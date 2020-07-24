# VirtualCompBot
VirtualCompBot is an application created to run the second Cubing At Home competition. It is currently being hosted at https://cubething.kikoho.xyz. If you have any questions you can contact geistmeister11@gmail.com.
<br><br>
## Running a Competition
All you need to create a competition is a google sheet with certain formatting. You can get the formatting here: https://docs.google.com/spreadsheets/d/1YWisYkk5w2AojH4IQtcmehZkFAzlgTpVUdkwtqdyb-Y/copy.
<br>
### Create Events List
Once replacing all the placeholder data you will have to share the sheet with the service account <b>cubingbot@cubingbot-279013.iam.gserviceaccount.com</b>. 
You can then go to https://cubething.kikoho.xyz/url and put in the link to the google sheets module from your address bar and the name of the sheet where your events are stored. This will create the link you will give to your competitors that references back to that module and sheet.
### Managing Events
You can select which events show in the events list by the changing text in the second row to <b>ON</b> or <b>OFF</b>. Make sure each column is named differently. If two columns share the same name, the program will only be able to recognize one of them. The scrambles column must be directly to right of the main column and the scrambles images column directly to the right of that. There can be as much or as little spacing between each event cluster as desired.
### Seeing Reults
When times have been submitted they will be put into a sheet with the same name as the event. The times will noted in terms of seconds and sorted by when they are  entered. 
### Formatting Times
When all times have been submitted for an event you can format the times to a more readable format. Using https://cubething.kikoho.xyz/format, put the link to the google sheets module and the name of the event in the website. When you submit, a new sheet will be created with the name of your event + (r) (ex: 3x3 R1(r)). This sheet will be sorted by best time and have the average of five and place displayed.
<br>
## License
MIT  © Tyler Geist
