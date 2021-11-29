TableSchema= \
{
	"definitions": {},
	"$schema": "http://json-schema.org/draft-07/schema#", 
	"$id": "https://example.com/object1638174336.json", 
	"title": "Root", 
	"type": "array",
	"default": [],
	"items":{
		"$id": "#root/items", 
		"title": "Items", 
		"type": "object",
		"required": [
			"name",
			"type"
		],
		"properties": {
			"name": {
				"$id": "#root/items/name", 
				"title": "Name", 
				"type": "string",
				"default": "",
				"examples": [
					"[NAME]"
				],
				"pattern": "^.*$"
			},
			"type": {
				"$id": "#root/items/type", 
				"title": "Type", 
				"type": "string",
				"default": "",
				"examples": [
					"[TYPE]"
				],
				"pattern": "^.*$"
			}
		}
	}

}