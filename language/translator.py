
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
            root_locale='ru'
        )

    def __call__(self, language: str, *args, **kwds):
        return LocalizedTranslator(
            translator=self.t_hub.get_translator_by_locale(locale=language)
        )



class LocalizedTranslator:
    translator: TranslatorRunner

    def __init__(self, translator: TranslatorRunner) -> None:
        self.translator = translator

    def get(self, key: str):
        return self.translator.get(key)