
from aiogram.types import file
from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator, TranslatorRunner

class Translator:
    t_hub: TranslatorHub

    def __init__(self) -> None:
        self.t_hub = TranslatorHub(
            locales_map={
                "en": ("en", "ru", ),
                "ru": ("ru", )
            },
            # Добавляем файлы с языками к каждому переводу, например к 'en' будет файл с английским переводом 'en.ftl'
            translators=[
                FluentTranslator(
                    locale='en',
                    translator=FluentBundle.from_files(
                        locale='en-US', filenames=['en.ftl', ]
                    ),
                ),

                FluentTranslator(
                    locale='ru',
                    translator=FluentBundle.from_files(
                        locale='ru-RU', filenames=['ru.ftl', ]
                    ),
                ),
            ],
            root_locale='ru' # если в базе какой-то неизвестный язык, то вместо него будет русский
        )

    def __call__(self, language: str, *args, **kwds):
        return LocalizedTranslator(
            # Метод, который выбирает перевод под конкретный locale 'ru' либо 'en'
            translator=self.t_hub.get_translator_by_locale(locale=language)
        )


# Переводчик под конкретный язык
class LocalizedTranslator:
    translator: TranslatorRunner

    def __init__(self, translator: TranslatorRunner) -> None:
        self.translator = translator

    # получаем значение переменных в файлах .ftl
    def get(self, key: str):
        return self.translator.get(key)