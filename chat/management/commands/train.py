from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer

class Command(BaseCommand):
    help = "Training the chatbot"

    def handle(self, *args, **options):
        chatterbot = ChatBot(**settings.CHATTERBOT)
        trainer = ListTrainer(chatterbot)
        trainer.train(
            [
                "Hello",
                "Hello there! how may i help you",
                "Hi",
                "Hi there, how can i help you today",
                "Hey",
                "Hey there, how can i help you today",
                "Need a car",
                "I can help you choose a car according to the following type, please type any;Sedan SUV Crossover",
                "search for car"
                "I can help you choose a car according to the following type, please type any;Sedan SUV Crossover",
                "what can you do",
                "I can help you choose a car according to the following type, please type any;Sedan SUV Crossover",
                "how can you help",
                "I can help you choose a car according to the following type, please type any;Sedan SUV Crossover",
                "Sedan"
                "There are seven Car Makes to select from, please type any of the following. Example Toyota sedan\n" \
                "Toyota\n"\
                "Nissan\n"\
                "Honda\n"\
                "Audi\n"\
                "BMW\n"\
                "Subaru", 
                "Toyota sedan",
                "The following Toyota cars can be classified as Toyota sedan;\n"\
                "Toyota Camry\n"\
                "Toyota Corolla\n"\
                "Toyota Avalon\n"\
                "Toyota Yaris\n"\
                "Toyota Crown", 
                "Nissan Sedan",
                "The following Nissan cars can be classified as Nissan sedan;\n"\
                "Nissan Tiida\n"\
                "Nissan Latio\n"\
                "Nissan Skyline\n"\
                "Nissan Sylphy\n"\
                "Nissan Teana\n"\
                "Nissan Fuga\n"\
                "Nissan Bluebird",
                "Honda sedan",
                "The following Honda car can be classified as Honda sedan;\n"\
                "Honda Grace\n"\
                "Honda Inspire\n"\
                "Honda Accord\n"\
                "Honda Insight",
                "BMW sedan",
                "The following BMW cars can be classified as BMW sedan;\n"\
                "BMW 3 series\n"\
                "BMW 5 series",
                "AUDI sedan",
                "The following AUDI cars can be classified as AUDI sedan;\n"\
                "AUDI A3\n"\
                "AUDI A4\n"\
                "AUDI A5\n"\
                "AUDI A6\n"\
                "AUDI S3\n"\
                "AUDI S4\n"\
                "AUDI S5",
                "Subaru sedan",
                "The following Subaru cars can be classified as SUBARU sedan;\n"\
                "Subaru Impreza\n"\
                "Subaru Legacy\n"\
                "Subaru WRX",
                "SUV",
                "There are seven Car Makes to select from, please type any of the following. Example Toyota SUV\n"\
                "Toyota\n"\
                "Nissan\n"\
                "Honda\n"\
                "Audi\n"\
                "BMW\n"\
                "Subaru",
                "Toyota SUV",
                "The following Toyota cars can be classified as Toyota SUV;\n"\
                "Toyota Prado\n"\
                "Toyota LC 300\n"\
                "Toyota LC 200\n"\
                "Toyota Fortuner\n"\
                "Toyota 4Runner\n"\
                "Toyota Highlander",
                "Nissan SUV",
                "The following Nissan cars can be classified as Nissan SUV;\n"\
                "Nissan Patrol\n"\
                "Nissan Xtrail",
                "Honda SUV",
                "The following Honda cars can be classified as Honda SUV;\n"\
                "Honda CR-V\n"\
                "Toyota Pilot\n"\
                "Toyota HR-V\n"\
                "Toyota Passport",
                "AUDI SUV",
                "The following AUDI cars can be classified as AUDI SUV;\n"\
                "AUDI Q3\n"\
                "AUDI Q5\n"\
                "AUDI Q7",
                "BMW SUV",
                "The following BMW cars can be classified as BMW SUV;\n"\
                "BMW X1\n"\
                "BMW X3\n"\
                "BMW X5\n"\
                "BMW X6",
                "Subaru SUV",
                "The following Subaru cars can be classified as Subaru SUV;\n"\
                "Subaru Forester\n"\
                "Subaru Outback",
                "Crossover",
                "There are seven Car Makes to select from, please type any of the following. Example Toyota Crossover;\n"\
                "Toyota\n"\
                "Nissan\n"\
                "Honda\n"\
                "Audi\n"\
                "BMW\n"\
                "Subaru",
                "Toyota Crossover", 
                "The following Toyota cars can be classified as Toyota Crossover;\n"\
                "Toyota Harrier\n"\
                "Toyota RAV4\n"\
                "Toyota VANGUARD\n"\
                "Toyota RUSH",
                "Nissan Crossover",
                "The following Nissan cars can be classified as Nissan Crossover;\n"\
                "Nissan Ariya\n"\
                "Nissan Rogue\n"\
                "Nissan Murani\n"\
                "Nissan Kick",
                "Honda Crossover", 
                "The following Honda cars can be classified as Honda Crossover;\n"\
                "Honda HR-V",
                "AUDI Crossover",
                "The following AUDI cars can be classified as AUDI Crossover;\n",
                "AUDI Q5\n"\
                "AUDI Q7",
                "BMW Crossover", 
                "The following BMW cars can be classified as BMW Crossover;\n"\
                "BMW X3\n"\
                "BMW X5",
                "Subaru Crossover",
                "The following Crossover cars can be classified as Subaru Crossover;\n"\
                "Subaru XV",
                "",
                "I can’t get you", 
                "kjfgfjgjtwwt",
                "I can’t get you",
                "1",
                "I can’t get you",
                "Thanks, thank you",
                "Welcome Again.",
                "Byee, See you", 
                "Byee"
                
                
            ]
        )
        self.stdout.write(self.style.SUCCESS("Successfull!"))