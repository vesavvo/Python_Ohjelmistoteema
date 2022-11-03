# Using external interfaces

In this module you will learn to use external Application Programming Interfaces (APIs).

Providers of public Internet services such as weather services and open databases make it possible
to use their publicly available resources in programs. The resources are accessed through an API.
The provider of a service decided the type of API it offers and how it is used. Using an API requires
for a programmer to become familiar with the documentation of the API.

## Sending requests

API requests follow the HTTP protocol. The protocol defines five general operations (or resource methods):

- GET retrieves/reads a data object
- PUT replaces an existing data object
- POST creates a new data object
- PATCH modifies an existing data object
- DELETE deletes an existing data object

The GET operation is the same operation that is used for regular web page requests. If an interface is designed
to follow the so called REST API design practices, all five operations listed here can be used. The RESTful design
specification also follows other design principles that are not discussed here.

The specification of an effective API can also be based on only the GET operation, but in that case, it is
not considered a true REST API. On this course we will explore the use and implementation of an API that is based on
the GET operation.

As an example, let's look at how to use the API provided by the TVmaze service. The API documentation can be found here:
https://www.tvmaze.com/api.

TVmaze offers a public open API that does not require a user account to use. These types of APIs usually only allow 
read operations. Read operations are performed with GET requests.

Our goal is to write a Python program that fetches all TV programs that include a string of text written by the user. 
Based on the documentation of the TVmaze API this type of an API request should be given in the format of 
`URL: /search/shows?q=:query` and an example of such request would be https://api.tvmaze.com/search/shows?q=girls.

The operation of the request should first be tested by writing the request statement to the address bar of a web browser
(such as Chrome). Typically, it is only possible to send GET requests via a browser.

From a Python program a similar request is sent using the `get` method from the `requests` library.
Applying the `json` method to the received response converts the data to a Python dictionary structure:

```python
import requests

keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.tvmaze.com/search/shows?q=" + keyword
response = requests.get(request).json()
print(response)

```

Let's see how the program works:
```monospace
Enter keyword: python
[{'score': 0.6097852, 'show': {'id': 25376, 'url': 'https://www.tvmaze.com/shows/25376/python-hunters', 'name': 'Python Hunters', 'type': 'Reality', 'language': 'English', 'genres': ['Nature'], 'status': 'Ended', 'runtime': 60, 'averageRuntime': 60, 'premiered': '2010-07-12', 'ended': '2012-06-01', 'officialSite': None, 'schedule': {'time': '22:00', 'days': ['Monday']}, 'rating': {'average': None}, 'weight': 23, 'network': {'id': 42, 'name': 'National Geographic Channel', 'country': {'name': 'United States', 'code': 'US', 'timezone': 'America/New_York'}, 'officialSite': None}, 'webChannel': None, 'dvdCountry': None, 'externals': {'tvrage': None, 'thetvdb': 177341, 'imdb': 'tt1688573'}, 'image': {'medium': 'https://static.tvmaze.com/uploads/images/medium_portrait/363/909096.jpg', 'original': 'https://static.tvmaze.com/uploads/images/original_untouched/363/909096.jpg'}, 'summary': "<p>They have no natural predators; they eat four times as much as an alligator; and if they're not stopped, they could destroy one of America's most important ecosystems. Now an elite squad of three licensed hunters is fighting back. As they capture snakes, the <b>Python Hunters</b> look for clues to how the invaders came to be established in the Everglades. Popular perception is that the snakes are the progeny of family pets released into the wild by irresponsible owners no longer willing or able to care for them. The Python Hunters though consider a more likely explanation is an incident in 1992, when a greenhouse at the edge of the Everglades, housing over 900 Burmese Pythons, was destroyed by Hurricane Andrew.</p>", 'updated': 1633547701, '_links': {'self': {'href': 'https://api.tvmaze.com/shows/25376'}, 'previousepisode': {'href': 'https://api.tvmaze.com/episodes/1075377'}}}}, {'score': 0.47944784, 'show': {'id': 5068, 'url': 'https://www.tvmaze.com/shows/5068/monty-python-almost-the-truth', 'name': 'Monty Python: Almost the Truth', 'type': 'Documentary', 'language': 'English', 'genres': ['Comedy'], 'status': 'Ended', 'runtime': 60, 'averageRuntime': 60, 'premiered': '2009-10-18', 'ended': '2009-10-23', 'officialSite': None, 'schedule': {'time': '', 'days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}, 'rating': {'average': None}, 'weight': 43, 'network': {'id': 37, 'name': 'BBC Two', 'country': {'name': 'United Kingdom', 'code': 'GB', 'timezone': 'Europe/London'}, 'officialSite': 'https://www.bbc.co.uk/bbctwo'}, 'webChannel': None, 'dvdCountry': None, 'externals': {'tvrage': None, 'thetvdb': 118861, 'imdb': 'tt1422182'}, 'image': {'medium': 'https://static.tvmaze.com/uploads/images/medium_portrait/21/54341.jpg', 'original': 'https://static.tvmaze.com/uploads/images/original_untouched/21/54341.jpg'}, 'summary': '<p>Legendary British comedy troupe Monty Python all gathered in front of the camera one last time in this original documentary series that retells the entire Python phenomenon start to finish.</p>', 'updated': 1642386299, '_links': {'self': {'href': 'https://api.tvmaze.com/shows/5068'}, 'previousepisode': {'href': 'https://api.tvmaze.com/episodes/315335'}}}}, {'score': 0.3801934, 'show': {'id': 41604, 'url': 'https://www.tvmaze.com/shows/41604/mytho', 'name': 'Mytho', 'type': 'Scripted', 'language': 'French', 'genres': ['Drama', 'Comedy'], 'status': 'Ended', 'runtime': 52, 'averageRuntime': 52, 'premiered': '2019-10-10', 'ended': '2021-09-30', 'officialSite': 'https://www.arte.tv/fr/videos/RC-021458/mytho/', 'schedule': {'time': '', 'days': []}, 'rating': {'average': None}, 'weight': 47, 'network': {'id': 414, 'name': 'ARTE', 'country': {'name': 'France', 'code': 'FR', 'timezone': 'Europe/Paris'}, 'officialSite': None}, 'webChannel': None, 'dvdCountry': None, 'externals': {'tvrage': None, 'thetvdb': 361569, 'imdb': 'tt10677432'}, 'image': {'medium': 'https://static.tvmaze.com/uploads/images/medium_portrait/265/662931.jpg', 'original': 'https://static.tvmaze.com/uploads/images/original_untouched/265/662931.jpg'}, 'summary': '<p>Devoted mother and wife, Elvira feels more and more invisible to her family. One day, she gives into temptation and becomes caught up in a dreadful web of lies in her quest for love and attention.</p>', 'updated': 1635887033, '_links': {'self': {'href': 'https://api.tvmaze.com/shows/41604'}, 'previousepisode': {'href': 'https://api.tvmaze.com/episodes/2204496'}}}}, {'score': 0.34326607, 'show': {'id': 694, 'url': 'https://www.tvmaze.com/shows/694/monty-pythons-flying-circus', 'name': "Monty Python's Flying Circus", 'type': 'Variety', 'language': 'English', 'genres': ['Comedy'], 'status': 'Ended', 'runtime': 30, 'averageRuntime': 30, 'premiered': '1969-10-05', 'ended': '1974-12-05', 'officialSite': None, 'schedule': {'time': '22:00', 'days': ['Thursday']}, 'rating': {'average': 8.4}, 'weight': 83, 'network': {'id': 12, 'name': 'BBC One', 'country': {'name': 'United Kingdom', 'code': 'GB', 'timezone': 'Europe/London'}, 'officialSite': 'https://www.bbc.co.uk/bbcone'}, 'webChannel': None, 'dvdCountry': None, 'externals': {'tvrage': 4522, 'thetvdb': 75853, 'imdb': 'tt0063929'}, 'image': {'medium': 'https://static.tvmaze.com/uploads/images/medium_portrait/5/14980.jpg', 'original': 'https://static.tvmaze.com/uploads/images/original_untouched/5/14980.jpg'}, 'summary': "<p>And now for something completely different: <b>Monty Python's Flying Circus</b> was simply the most influential comedy program television has ever seen. Five Englishmen, all working under the constraints of conventional TV shows such as The Frost Report (for which the five Englishmen wrote), gathered together with an expatriate American in the spring of 1969 to break the rules. The result, first airing on BBC-1 on October 5, 1969, has influenced countless future men and women in the media and comedy since.</p>", 'updated': 1627558818, '_links': {'self': {'href': 'https://api.tvmaze.com/shows/694'}, 'previousepisode': {'href': 'https://api.tvmaze.com/episodes/61242'}}}}, {'score': 0.31305113, 'show': {'id': 8595, 'url': 'https://www.tvmaze.com/shows/8595/peyton-place', 'name': 'Peyton Place', 'type': 'Scripted', 'language': 'English', 'genres': ['Drama'], 'status': 'Ended', 'runtime': 30, 'averageRuntime': 30, 'premiered': '1964-09-15', 'ended': '1969-06-02', 'officialSite': None, 'schedule': {'time': '21:30', 'days': ['Tuesday']}, 'rating': {'average': None}, 'weight': 32, 'network': {'id': 3, 'name': 'ABC', 'country': {'name': 'United States', 'code': 'US', 'timezone': 'America/New_York'}, 'officialSite': 'https://abc.com/'}, 'webChannel': None, 'dvdCountry': None, 'externals': {'tvrage': None, 'thetvdb': 77441, 'imdb': None}, 'image': {'medium': 'https://static.tvmaze.com/uploads/images/medium_portrait/30/76577.jpg', 'original': 'https://static.tvmaze.com/uploads/images/original_untouched/30/76577.jpg'}, 'summary': "<p><b>Peyton Place</b> was America's first truly successful primetime serial. The series was the brainchild of veteran producer Paul Monash. Impressed with the success of Britain's monster hit Coronation Street, Monash wanted to import that UK series; however, ABC executives felt that US audiences would not cotton to the thick British accents and kitchen-sink drama. Monash countered with a slightly revamped version of Peyton Place, which had been a wildly popular novel by Grace Metalious and subsequent Hollywood film starring Lana Turner and Diane Varsi. While the book and series centered on the pious, hypocritical behavior of New England residents, the TV series eschewed most of that lasciviousness and told the story of life in a small New England village. In many ways, the TV program resembled a dramatic version of The Andy Griffith Show, featuring a recurring cast of warm, sympathetic characters.</p>", 'updated': 1639006567, '_links': {'self': {'href': 'https://api.tvmaze.com/shows/8595'}, 'previousepisode': {'href': 'https://api.tvmaze.com/episodes/476232'}}}}, {'score': 0.3000992, 'show': {'id': 16441, 'url': 'https://www.tvmaze.com/shows/16441/patton-360', 'name': 'Patton 360', 'type': 'Documentary', 'language': 'English', 'genres': ['War', 'History'], 'status': 'Ended', 'runtime': 60, 'averageRuntime': 60, 'premiered': '2009-04-10', 'ended': '2009-06-28', 'officialSite': None, 'schedule': {'time': '21:00', 'days': ['Friday']}, 'rating': {'average': None}, 'weight': 27, 'network': {'id': 53, 'name': 'History', 'country': {'name': 'United States', 'code': 'US', 'timezone': 'America/New_York'}, 'officialSite': None}, 'webChannel': None, 'dvdCountry': None, 'externals': {'tvrage': None, 'thetvdb': 90061, 'imdb': 'tt1409728'}, 'image': {'medium': 'https://static.tvmaze.com/uploads/images/medium_portrait/54/137074.jpg', 'original': 'https://static.tvmaze.com/uploads/images/original_untouched/54/137074.jpg'}, 'summary': '<p>As the United States enters World War Two, General George S. Patton sees the opportunity to fulfill his destiny. This series illustrates his combat exploits. But at times it seems he faced greater challenges with his superiors and his off the field behavior than the potent German army.</p>', 'updated': 1644181315, '_links': {'self': {'href': 'https://api.tvmaze.com/shows/16441'}, 'previousepisode': {'href': 'https://api.tvmaze.com/episodes/752601'}}}}, {'score': 0.2963689, 'show': {'id': 19823, 'url': 'https://www.tvmaze.com/shows/19823/monty-pythons-personal-best', 'name': "Monty Python's Personal Best", 'type': 'Scripted', 'language': 'English', 'genres': ['Comedy'], 'status': 'Ended', 'runtime': 60, 'averageRuntime': 60, 'premiered': '2006-02-22', 'ended': '2006-03-08', 'officialSite': None, 'schedule': {'time': '', 'days': ['Wednesday']}, 'rating': {'average': None}, 'weight': 34, 'network': {'id': 85, 'name': 'PBS', 'country': {'name': 'United States', 'code': 'US', 'timezone': 'America/New_York'}, 'officialSite': None}, 'webChannel': None, 'dvdCountry': None, 'externals': {'tvrage': None, 'thetvdb': 279855, 'imdb': 'tt0795156'}, 'image': {'medium': 'https://static.tvmaze.com/uploads/images/medium_portrait/69/174945.jpg', 'original': 'https://static.tvmaze.com/uploads/images/original_untouched/69/174945.jpg'}, 'summary': "<p><b>Monty Python's Personal Best</b> is a miniseries of six one-hour specials, each showcasing the contributions of a particular Monty Python member. Produced by Python (Monty) Pictures Ltd., the series first aired on PBS stations 22 February 2006, though two episodes were initially released on Region 1 DVD in 2005; the remaining episodes were released in late February 2006. The five surviving members (Eric Idle, Terry Jones, Terry Gilliam, Michael Palin and John Cleese) were invited to select favourite sketches they wrote or starred in, from the Monty Python's Flying Circus TV series as well as the troupe's films. All five collaborated on the sixth episode, a tribute to deceased Python Graham Chapman.</p>", 'updated': 1642386138, '_links': {'self': {'href': 'https://api.tvmaze.com/shows/19823'}, 'previousepisode': {'href': 'https://api.tvmaze.com/episodes/886748'}}}}, {'score': 0.29189575, 'show': {'id': 34625, 'url': 'https://www.tvmaze.com/shows/34625/peyton-and-polizzis-restaurant-rescue', 'name': "Peyton and Polizzi's Restaurant Rescue", 'type': 'Documentary', 'language': 'English', 'genres': [], 'status': 'Ended', 'runtime': 60, 'averageRuntime': 60, 'premiered': '2018-02-07', 'ended': '2021-02-28', 'officialSite': 'http://www.channel5.com/show/peyton-and-polizzis-restaurant-rescue/', 'schedule': {'time': '21:00', 'days': ['Wednesday']}, 'rating': {'average': None}, 'weight': 60, 'network': {'id': 135, 'name': 'Channel 5', 'country': {'name': 'United Kingdom', 'code': 'GB', 'timezone': 'Europe/London'}, 'officialSite': 'https://www.channel5.com/'}, 'webChannel': None, 'dvdCountry': None, 'externals': {'tvrage': None, 'thetvdb': None, 'imdb': None}, 'image': {'medium': 'https://static.tvmaze.com/uploads/images/medium_portrait/145/362889.jpg', 'original': 'https://static.tvmaze.com/uploads/images/original_untouched/145/362889.jpg'}, 'summary': "<p><b>Peyton and Polizzi's Restaurant Rescue</b> puts Alex Polizzi in the path of people whose dream to run their own restaurant has turned into an inexplicable nightmare. With Oliver Peyton's help, she'll set out to see if she can change the fortunes of struggling restaurant businesses.</p><p>From staffing to menus, service and décor, Alex, with the help of Oliver, will be on a quest to transform four struggling restaurants into successful and profitable ventures. Alex will draw on her career in the hospitality business to offer critique, advice and guidance, all served up with a large helping of her famously efficient, no-nonsense attitude. She'll ask Oliver Peyton to marshal the kitchens and critique the food, all in a bid to get the businesses to run with military precision.</p>", 'updated': 1631493183, '_links': {'self': {'href': 'https://api.tvmaze.com/shows/34625'}, 'previousepisode': {'href': 'https://api.tvmaze.com/episodes/2169352'}}}}, {'score': 0.27176368, 'show': {'id': 17742, 'url': 'https://www.tvmaze.com/shows/17742/pablo-escobar-el-patron-del-mal', 'name': 'Pablo Escobar: El Patrón del Mal', 'type': 'Scripted', 'language': 'Spanish', 'genres': ['Drama'], 'status': 'Ended', 'runtime': None, 'averageRuntime': None, 'premiered': '2012-05-28', 'ended': '2012-11-19', 'officialSite': None, 'schedule': {'time': '', 'days': []}, 'rating': {'average': None}, 'weight': 75, 'network': {'id': 1002, 'name': 'Caracol Televisión', 'country': {'name': 'Colombia', 'code': 'CO', 'timezone': 'America/Bogota'}, 'officialSite': None}, 'webChannel': None, 'dvdCountry': None, 'externals': {'tvrage': None, 'thetvdb': 259730, 'imdb': 'tt2187850'}, 'image': {'medium': 'https://static.tvmaze.com/uploads/images/medium_portrait/59/149372.jpg', 'original': 'https://static.tvmaze.com/uploads/images/original_untouched/59/149372.jpg'}, 'summary': '<p><b>Pablo Escobar: El Patrón del Mal</b> (Pablo Escobar: The King of Evil) is a fictional series product of free adaptation of "The Parable of Paul," Alonso Salazar, press articles and publicly known facts of national life, the historical facts are surrounded by fictional characters and dialogue, allowing supply and re-documented situations.</p>', 'updated': 1501048034, '_links': {'self': {'href': 'https://api.tvmaze.com/shows/17742'}, 'previousepisode': {'href': 'https://api.tvmaze.com/episodes/809913'}}}}, {'score': 0.238284, 'show': {'id': 47970, 'url': 'https://www.tvmaze.com/shows/47970/segitseg-itthon-vagyok', 'name': 'Segítség! Itthon vagyok!', 'type': 'Scripted', 'language': 'Hungarian', 'genres': ['Comedy'], 'status': 'Ended', 'runtime': 45, 'averageRuntime': 35, 'premiered': '2020-04-19', 'ended': '2020-05-31', 'officialSite': 'https://rtl.hu/rtlklub/segitseg-itthon-vagyok', 'schedule': {'time': '19:15', 'days': ['Sunday']}, 'rating': {'average': None}, 'weight': 16, 'network': {'id': 426, 'name': 'RTL Klub', 'country': {'name': 'Hungary', 'code': 'HU', 'timezone': 'Europe/Budapest'}, 'officialSite': None}, 'webChannel': None, 'dvdCountry': None, 'externals': {'tvrage': None, 'thetvdb': 380392, 'imdb': 'tt12171868'}, 'image': None, 'summary': None, 'updated': 1594052520, '_links': {'self': {'href': 'https://api.tvmaze.com/shows/47970'}, 'previousepisode': {'href': 'https://api.tvmaze.com/episodes/1873329'}}}}]
```

The request was sent successfully, and response is received. The JSON-type response must be processed so
that we can print out the information we want.

## Processing the response

Above the JSON response was stored in a variable called `response`. A function called `json.dumps` can
be used to clarify the structure of the response data. It modifies the structure of the response so that 
it is easier to read. Let's replace the printing statement with:

```python
print(json.dumps(response, indent=2))
```

For this, we must add an `import` statement to the start of the program:
```python
import json
```

Now the structure of the response is easier to understand. This is what the start of the response looks like:

```json
[
  {
    "score": 0.6097852,
    "show": {
      "id": 25376,
      "url": "https://www.tvmaze.com/shows/25376/python-hunters",
      "name": "Python Hunters",
      "type": "Reality",
      "language": "English",
      "genres": [
        "Nature"
      ],
```

Here we see that the items in the resulting list are programs and each of the programs are presented
as a dictionary structure. Each dictionary has the key `show` where the corresponding value is another
dictionary. The inner dictionary has the key `name` where the value contains a string of the name of the
TV program. As an example, the name of the first item on the `response` list could be referenced with the
expression `response[0][show][name]`.

Now we can replace the printing statement in the program with a `for` loop that prints out the name of each
of the found programs.

```python
for a in response:
    print(a["show"]["name"])
```

The start of the output looks as follows:

```monospace
Python Hunters
Monty Python: Almost the Truth
Mytho
Monty Python's Flying Circus
```

## Error handling

The above program that uses an external API only works when the external service (in this case TV Maze) is operational
an manages to execute the request it receives. As we are dealing with an external service, we cannot trust that the
service always works. Let's extend our program by adding necessary error checks so that we can program errors to be handled
in the way we want.

Error handling here is based on two factors:
1. The HTTP status code received with the response
2. Handling on exceptions that occur in the Python program

When the external service is operational, it returns an HTTP status code with the response. The status code is 200
when the request is successfully fulfilled. A failed request is responded with a status code that best describes
the error that occured. The official list of HTTP response status codes can be found on the World Wide Web Consortium (W3C) 
web page at: https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html. The status code can be read in the program from the
`status_code` property returned by the `request.get` method. Here we will limit the error testing by only checking whether the
status code is 200 or something else.

Sometimes there can be a situation where the external service cannot be reached at all and as a result cannot even
return a status code that would show an error. This manifests as the Python program crashing during runtime, running to a so called
runtime error. In Python it is possible to program the exception handling yourself leaving it for the programmer to decide what
should happen when an exception occurs. Exception handling is done using a `try/except` structure.

Let's extend the program by adding a check for HTTP status code 200 and an exception handling routine for any exceptions raised by the `request` library.

Each Python exception is an object. Especially exceptions raised by the `requests` library are instances from classes derived from the `RequestException`
base class. With added error handling the program now looks like this:

```python
import json
import requests

keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.tvmaze.com/search/shows?q=" + keyword

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        # print(json.dumps(json_response, indent=2))
        for a in json_response:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")
```

Let's see what happens when a request fails. We will change the request on purpose by adding a typo
in the URL. The domain code is now `cob` instead of `com`, which should produce an error:

```python
request = "https://api.tvmaze.cob/search/shows?q=" + keyword
```
Now the program does not crash when an error occurs, but works as we have programmed it do:
```monospace
Enter keyword: python
Request could not be completed.
```

In the end we of course fix the URL. Because of exception handling we are now prepared for
situation where TV Maze would for example be out of use due to a maintenance break. Programming
best practices include adding this type of error handling into programs.
