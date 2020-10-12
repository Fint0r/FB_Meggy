#!/usr/bin/python3
from fbchat import Client


class EchoBot(Client):
    meggy_counter = 0
    jatekosok = []
    code = ''

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        if author_id != self.uid:
            sender_name = self.fetchUserInfo(author_id)[author_id].name

            if 'kód:' in message_object.text or 'Kód:' in message_object.text or 'kod:' in message_object.text or 'Kod:' in message_object.text:
                self.code = message_object.text.split(':')[1].strip()
                message_object.text = f'Kód {self.code} mentve.'
                self.send(message_object, thread_id=thread_id, thread_type=thread_type)
            if message_object.text == '-':
                if sender_name in self.jatekosok:
                    self.jatekosok.remove(sender_name)
                    self.meggy_counter -= 1
                    names = '\n'.join(self.jatekosok)
                    message_object.text = f'Játszani akarók száma: {str(self.meggy_counter)}\n{names}'
                    if self.meggy_counter > 5:
                        message_object.text += 'Megvagyunk!'
                    self.send(message_object, thread_id=thread_id, thread_type=thread_type)
                else:
                    message_object.text = 'Tudjuk, hogy rád sosem számíthatunk...'
                    self.send(message_object, thread_id=thread_id, thread_type=thread_type)

            if message_object.text == '€':
                message_object.text = 'Fintor gyere vedelni!'
                self.send(message_object, thread_id=thread_id, thread_type=thread_type)

            if message_object.text == 'reset' or message_object.text == 'Reset' or message_object.text == 'Clear' or message_object.text == 'clear':
                self.meggy_counter = 0
                self.jatekosok = []
                self.code = ''
                message_object.text = 'Reseteltem a countert!'
                self.send(message_object, thread_id=thread_id, thread_type=thread_type)

            if message_object.text == 'help' or message_object.text == 'Help':
                message_object.text = '🍒 - Ha játszanál\nReset, Clear - Ha vége a játéknak\nKód: ABCDEQ - Ha mentenéd a kódot\n- - Ha mégsem jössz\nEmergency meeting, EM - Ha kevesen vagyunk\n€ - Ha inni kell\nTimo vacsora! - Ha Timo éhes\nSalty - Ha hülye vagy'
                self.send(message_object, thread_id=thread_id, thread_type=thread_type)

            if message_object.text == '🍒':
                if sender_name not in self.jatekosok:
                    self.jatekosok.append(sender_name)
                    self.meggy_counter += 1
                    names = '\n'.join(self.jatekosok)
                    if self.code != '':
                        message_object.text = f'Játszani akarók száma: {str(self.meggy_counter)}\nJátékkód: {self.code}\n{names}'
                    else:
                        message_object.text = f'Játszani akarók száma: {str(self.meggy_counter)}\n{names}'
                    if self.meggy_counter > 5:
                        message_object.text += 'Megvagyunk!'
                    self.send(message_object, thread_id=thread_id, thread_type=thread_type)
                else:
                    message_object.text = 'Te már jelentkeztél a játékra!'
                    self.send(message_object, thread_id=thread_id, thread_type=thread_type)


client = EchoBot('', '')
client.listen()
