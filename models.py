from peewee import Model, SqliteDatabase, CharField, TextField

db = SqliteDatabase('translations.db')

class TranslationModel(Model):
    text = TextField()
    starting_language = CharField()
    target_language = CharField()
    translation = TextField(null=True)

    class Meta:
        database = db

db.create_tables([TranslationModel])
