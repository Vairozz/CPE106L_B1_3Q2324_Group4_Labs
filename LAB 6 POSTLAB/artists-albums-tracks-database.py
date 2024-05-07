from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["artists-albums-tracks_database"]

media_types = db["media_types"]
genres = db["genres"]
playlists = db["playlists"]
playlist_track = db["playlist_track"]
artists = db["artists"]
albums = db["albums"]
employees = db["employees"]
customers = db["customers"]
invoices = db["invoices"]
invoice_items = db["invoice_items"]
tracks = db["tracks"]

playlists_schema = {"PlaylistId": 1, "Name": 1}
playlist_track_schema = {"PlaylistId": 1, "TrackId": 1}
artists_schema = {"ArtistID": 1, "Name": 1}
albums_schema = {"AlbumID": 1, "Title": 1, "ArtistId": 1}
employees_schema = {"EmployeeID": 1, "LastName": 1, "FirstName": 1, "Title": 1, "ReportsTo": 1, "Birthdate": 1, "HireDate": 1, "Address": 1}
customers_schema = {"CustomerID": 1, "FirstName": 1, "LastName": 1, "Company": 1, "Address": 1, "City": 1, "State": 1, "Country": 1, 
                    "PostalCode": 1, "Phone": 1, "Fax": 1, "Email": "@gmail.com", "SupportRepId": 1}
invoices_schema = {"InvoiceID": 1, "CustomerId": 1, "InvoiceDate": 1, "Billingaddress": 1, "BillingCity": 1}
invoice_items_schema = {"Invoiceltemld": 1, "InvoiceID": 1, "TrackID": 1, "UnitPrice": 1, "Quantity": 1}
tracks_schema = {"TrackID": 1, "Name": "NAMEs", "AlbumId": 1, "MediaTypeID": 1, "Genreld": 1, 
                 "Composer": 1, "Milliseconds": 1, "Bytes": 1, "UnitPrice": 1}

playlists.insert_one(playlists_schema)
playlist_track.insert_one(playlist_track_schema)
artists.insert_one(artists_schema)
albums.insert_one(albums_schema)
employees.insert_one(employees_schema)
customers.insert_one(customers_schema)
invoices.insert_one(invoices_schema)
invoice_items.insert_one(invoice_items_schema)
tracks.insert_one(tracks_schema)

media_types.insert_one({"MediaTypeId": tracks_schema, "Name": "New Album"})
genres.insert_one({"GenreID": tracks_schema, "Name": "New Album"})
