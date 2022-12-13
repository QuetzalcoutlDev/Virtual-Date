
# Virtual Date! 
# Copyright (C) 2022 QuetzalcoutlDev

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from source import config

# Este archivo contiene todas los temás de conversación
# los cumplidos, etc.

types_es = {

            "types":
                    [
                    "Hablar...", 
                    # "Quiero decirte algo...",
                    "Me siento...",
                    "Hacer una pregunta...",
                    "Hacer un cumplido...",
                    "Adiós."
                    ],

            "labels":
                    [
                    "0",
                    # "1",
                    "2",
                    "3",
                    "4",
                    "5"
                    ]

            }

types_en = {

            "types":
                    [
                    "Speak...",
                    # "I want to tell you something...",
                    "I feel...",
                    "Ask a question...",
                    "Make a compliment...",
                    "Bye."
                    ],

            "labels":
                    [
                    "0",
                    # "1",
                    "2",
                    "3",
                    "4",
                    "5"
                    ]

            }

types_labels_es = {
            
                    "5":
                        [
                        ["normal", "¿Ya te vas?", "normal", None],
                        ["embarrassed", "Que mal.", "normal", None],
                        ["normal", "Bueno, entonces nos vemos después.", "normal", None],
                        ["normal", "Me encargare de guardar tu progreso.", "excuse", None],
                        ["happy", "Espero verte de nuevo.", "normal", None],
                        ["happy", "Adiós.", "hi", None],
                        ["happy", "", "hi", "quit"]
                        ]

                    }

types_labels_en = {
            
                    "5":
                        [
                        ["normal", "Are you leaving yet?", "normal", None],
                        ["embarrassed", "Too bad.", "normal", None],
                        ["normal", "Okay, see you later then.", "normal", None],
                        ["normal", "I'll take care of saving your progress.", "excuse", None],
                        ["happy", "Hope to see you again.", "normal", None],
                        ["happy", "Bye.", "hi", None],
                        ["happy", "", "hi", "quit"]
                        ]

                }

###########################
## Cumplidos/compliments ##
###########################

make_compliments_es = {

                        "types":
                                [
                                "Eres muy bonita.",
                                "Me gusta tú cabello.",
                                "Me gusta el color de tus ojos.",
                                "Eres muy inteligente.",
                                "Eres increíble.",
                                "Amo el sonido de tu voz.",
                                "Tienes una bonita figura.",
                                "Te ves bien con esa pañoleta.",
                                "Me gusta cómo te ves con esa ropa.",
                                "Atrás."
                                ],

                        "labels":
                                [
                                "0",
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "9"
                                ]
                        }

make_compliments_en = {

                    "types":
                            [
                            "You are very pretty.",
                            "I like your hair.",
                            "I like the color of your eyes.",
                            "You are very smart.",
                            "You are amazing.",
                            "I love the sound of your voice.",
                            "You have a nice figure.",
                            "You look good with that scarf.",
                            "I like how you look in those clothes.",
                            "Behind."
                            ],

                        "labels":
                                [
                                "0",
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "9"
                                ]
                        }

compliments_labels_es = {
                    
                        "0":
                            [
                            ["embarrassed", "Aww~", "normal", None],
                            ["embarrassed", "Gracias.", "normal", None],
                            ["happy", "¿Qué tan bonita crees que soy?", "normal", None],
                            ["happy", "Jeje.", "normal", None],
                            ["happy", "", "normal", "exp:2"]
                            ],

                        "1": 
                            [
                            ["normal", "Oh, ¿Enserio?", "normal", None],
                            ["happy", "Muchas gracias.", "normal", None],
                            ["normal", "Aunque no sé si sabes...", "normal", None],
                            ["normal", "Pero cuidar mi cabello es bastante difícil.", "date", None],
                            ["normal", "Tengo que comprar algunos shampoo específicos para mantenerlo suave y sedoso.", "date", None],
                            ["normal", "Porque si no puedo dañarlo.", "normal", None],
                            ["normal", "Así que espera verme siempre con el cabello suave y muy sedoso.", "excuse", None],
                            ["happy", "Me gusta mucho cuidar de mi cabello, jeje.", "normal", None],
                            ["happy", "", "normal", "exp:3"]
                            ],

                        "2": 
                            [
                            ["happy", "Gracias.", "normal", None],
                            ["happy", "El color de mis ojos es por lo que muchas personas me conocen.", "normal", None],
                            ["normal", "Quizá no sea una de mis cualidades más notables...", "excuse", None],
                            ["normal", "Pero me gusta el hecho de que muchas personas me elogien por ellos.", "normal", None],
                            ["happy", "Quizás tú también tengas un color de ojos muy bonito.", "normal", None],
                            ["normal", "Por cierto...", "normal", None],
                            ["happy", "Sabías que los ojos son la ventana al alma.", "excuse", None],
                            ["happy", "Es un pensamiento muy bonito, ¿No lo crees?", "excuse", None],
                            ["happy", "", "normal", "exp:5"]
                            ],
                        "3": 
                            [
                            ["jeje", "¿Muy inteligente, yo?", "normal", None],
                            ["happy", "No, cómo crees, no soy tan inteligente.", "normal", None],
                            ["happy", "Se muchas cosas pero no soy tan inteligente.", "excuse", None],
                            ["normal", "Soy muy torpe.", "normal", None],
                            ["happy", "Quizás tú seas más inteligente que yo.", "date", None],
                            ["happy", "", "normal", "exp:2"]
                            ],
                        "4": 
                            [
                            ["happy", "Es increíble que me digas que soy increíble.", "normal", None],
                            ["happy", "Jeje.", "normal", None],
                            ["happy", "Tú también debes de ser muy increíble.", "normal", None],
                            ["happy", "", "normal", "exp:3"]
                            ],
                        "5": 
                            [
                            ["jeje", "¿Te gusta el sonido de mi voz?", "normal", None],
                            ["happy", "¿Cómo te puede gustar si ni siquiera tengo voz?", "normal", None],
                            ["normal", "Aunque en futuras actualizaciones del juego puedo tenerla.", "excuse", None],
                            ["happy", "Dime, ¿Conoces o tienes una amiga japonesa que quiera darme voz?", "excuse", None],
                            ["happy", "Jeje.", "normal", None],
                            ["happy", "Si tienes una amiga que quiera darme voz seria genial.", "normal", None],
                            ["happy", "", "normal", "exp:2"]
                            ],
                        "6": 
                            [
                            ["oh", "Oh~.", "normal", None],
                            ["oh", "¿Así que has estado admirando mi figura?", "normal", None],
                            ["oh", "Sabes...", "normal", None],
                            ["oh", "Soy muy conocida por tener una buena figura.", "date", None],
                            ["happy", "Jeje.", "normal", None],
                            ["happy", "Me esfuerzo cada día por cuidar de mi cuerpo.", "normal", None],
                            ["happy", "No hago mucha dieta, porque lo que se pierde en un mes se recupera en una semana.", "excuse", None],
                            ["normal", "Lo que hago es salir a correr por las mañanas durante una hora.", "excuse", None],
                            ["normal", "No como mucha carne, pero a veces si lo hago.", "excuse", None],
                            ["happy", "También cuido mi alimentación y no como mucha comida chatarra.", "normal", None],
                            ["jeje", "Aunque quiero aclarar que a veces si lo hago.", "excuse", None],
                            ["happy", "Y así me mantengo saludable y con una bonita figura.", "normal", None],
                            ["normal", "Y dime...", "normal", None],
                            ["normal", "¿Tú también cuidas de tu cuerpo?", "excuse", None],
                            ["normal", "", "normal", "exp:7"],
                            ],
                        "7": 
                            [
                            ["normal", "¿Hablas de lo que tengo en mi cabello?", "normal", None],
                            ["happy", "Bueno, si es así, agradezco el cumplido.", "normal", None],
                            ["normal", "La verdad me gusta el cómo se ve.", "normal", None],
                            ["happy", "Siento que me da personalidad.", "excuse", None],
                            ["happy","¿Tú que crees?", "excuse", None],
                            ["happy","", "normal", "exp:3"],
                            ],
                        "8": 
                            [
                            ["jeje", "Gracias, pero actualmente es la única que tengo.", "normal", None],
                            ["happy", "En futuras actualizaciones tendré más.", "normal", None],
                            ["hangry", "Espero que en este momento estés usando una ropa decente para hablar conmigo.", "normal", None],
                            ["happy", "No mentira.", "normal", None],
                            ["normal", "Debes usar la ropa que te gusta.", "normal", None],
                            ["normal", "La ropa de manera inconsciente que usamos es la que define nuestros gustos y estado emocional.", "date", None],
                            ["happy", "Por ejemplo yo estoy usando actualmente una camisa de color blanco.", "excuse", None],
                            ["happy", "Quiere decir que estoy muy feliz.", "normal", None],
                            ["happy", "Jeje.", "normal", None],
                            ["happy", "",  "normal", "exp:3"]
                            ],
                        }

compliments_labels_en = {
                    
                        "0":
                        [
                        ["embarrassed", "Aww~", "normal", None],
                        ["embarrassed", "Thanks.", "normal", None],
                        ["happy", "How pretty do you think I am?", "normal", None],
                        ["happy", "Hehe.", "normal", None],
                        ["happy", "", "normal", "exp:2"]
                        ],

                        "1":
                        [
                        ["normal", "Oh, really?", "normal", None],
                        ["happy", "Thank you very much.", "normal", None],
                        ["normal", "Although I don't know if you know...", "normal", None],
                        ["normal", "But taking care of my hair is quite difficult.", "date", None],
                        ["normal", "I have to buy some specific shampoo to keep it smooth and silky.", "date", None],
                        ["normal", "Because if I can't damage it.", "normal", None],
                        ["normal", "So expect to always see me with soft and very silky hair.", "excuse", None],
                        ["happy", "I really like taking care of my hair, hehe.", "normal", None],
                        ["happy", "", "normal", "exp:3"]
                        ],

                        "2":
                        [
                        ["happy", "Thank you.", "normal", None],
                        ["happy", "My eye color is what many people know me by.", "normal", None],
                        ["average", "Perhaps not one of my most notable qualities...", "excuse", None],
                        ["normal", "But I like the fact that many people praise me for them.", "normal", None],
                        ["happy", "Maybe you have a very pretty eye color too.", "normal", None],
                        ["normal", "By the way...", "normal", None],
                        ["happy", "Did you know that the eyes are the window to the soul.", "excuse", None],
                        ["happy", "That's a very nice thought, don't you think?", "excuse", None],
                        ["happy", "", "normal", "exp:5"]
                        ],
                        "3":
                        [
                        ["jeje", "Very smart, me?", "normal", None],
                        ["happy", "No, what do you think, I'm not that smart.", "normal", None],
                        ["happy", "I know a lot but I'm not that smart.", "excuse", None],
                        ["normal", "I'm very clumsy.", "normal", None],
                        ["happy", "Maybe you're smarter than me.", "date", None],
                        ["happy", "", "normal", "exp:2"]
                        ],
                        "4":
                        [
                        ["happy", "It's amazing that you tell me I'm awesome.", "normal", None],
                        ["happy", "Hehe.", "normal", None],
                        ["happy", "You must be pretty awesome too.", "normal", None],
                        ["happy", "", "normal", "exp:3"]
                        ],
                        "5":
                        [
                        ["jeje", "Do you like the sound of my voice?", "normal", None],
                        ["happy", "How can you like me if I don't even have a voice?", "normal", None],
                        ["normal", "Although in future game updates I may have it.", "excuse", None],
                        ["happy", "Tell me, do you know or have a Japanese friend who wants to give me a voice?", "excuse", None],
                        ["happy", "Hehe.", "normal", None],
                        ["happy", "If you have a friend who wants to give me a voice that would be great.", "normal", None],
                        ["happy", "", "normal", "exp:2"]
                        ],
                        "6":
                        [
                        ["oh", "Oh~.", "normal", None],
                        ["oh", "So you've been admiring my figure?", "normal", None],
                        ["oh", "You know...", "normal", None],
                        ["oh", "I'm well known for having a good figure.", "date", None],
                        ["happy", "Hehe.", "normal", None],
                        ["happy", "I strive every day to take care of my body.", "normal", None],
                        ["happy", "I don't diet much, because what is lost in a month is recovered in a week.", "excuse", None],
                        ["normal", "What I do is go jogging in the morning for an hour.", "excuse", None],
                        ["normal", "I don't eat a lot of meat, but sometimes I do.", "excuse", None],
                        ["happy", "I also watch my diet and don't eat a lot of junk food.", "normal", None],
                        ["jeje", "Although I want to clarify that sometimes I do.", "excuse", None],
                        ["happy", "And so I stay healthy and have a nice figure.", "normal", None],
                        ["normal", "And tell me...", "normal", None],
                        ["normal", "Do you also take care of your body?", "excuse", None],
                        ["normal", "", "normal", "exp:7"],
                        ],
                        "7":
                        [
                        ["normal", "Are you talking about what's in my hair?", "normal", None],
                        ["happy", "Well, if so, I appreciate the compliment.", "normal", None],
                        ["normal", "I really like how it looks.", "normal", None],
                        ["happy", "I feel like it gives me personality.", "excuse", None],
                        ["happy","What do you think?", "excuse", None],
                        ["happy","", "normal", "exp:3"],
                        ],
                        "8":
                        [
                        ["jeje", "Thanks, but it's currently the only one I have.", "normal", None],
                        ["happy", "In future updates I will have more.", "normal", None],
                        ["hangry", "I hope you're wearing decent clothes to talk to me right now.", "normal", None],
                        ["happy", "No lie.", "normal", None],
                        ["normal", "You should wear the clothes you like.", "normal", None],
                        ["normal", "The clothes we unconsciously wear are what define our tastes and emotional state.", "date", None],
                        ["happy", "For example I am currently wearing a white shirt.", "excuse", None],
                        ["happy", "It means that I am very happy.", "normal", None],
                        ["happy", "Hehe.", "normal", None],
                        ["happy", "", "normal", "exp:3"]
                        ],
                    }

#########################
## Preguntas/Questions ##
#########################

make_questions_es = {

                    "types":
                            [
                            "¿Cuantos años tienes?",
                            "¿De que país provienes?",
                            "¿Cuantos mides?",
                            "¿Te gusta el anime?",
                            "¿Cual es tú anime favorito?",
                            "¿Te gustan los videojuegos?",
                            "¿Te gusta la música?",
                            "¿Cual es tu artista favorito?",
                            "¿Sabes programar?",
                            "¿Por qué el 'Virtual Date!' se hizo en Pygame?",
                            "¿De donde provienen tus gustos y personalidad?",
                            "¿Habra actualizaciones de 'Virtual Date!'?",
                            "¿Qué softwares se usaron para crear 'Virtual Date!'?",
                            "Atrás."
                            ],

                    "labels":
                            [
                            "0",
                            "1",
                            "2",
                            "3",
                            "4",
                            "5",
                            "6",
                            "7",
                            "8",
                            "9",
                            "10",
                            "11",
                            "12",
                            "13"
                            ]
                    }

make_questions_en = {

                    "types":
                            [
                            "How old are you?",
                            "What country are you from?",
                            "How tall are you?",
                            "Do you like anime?",
                            "What is your favorite anime?",
                            "You like video games?",
                            "Do you like music?",
                            "Who is your favorite artist?",
                            "Do you know how to program?"
                            "Why the 'Virtual Date!' was made in Pygame?",
                            "Where do your tastes and personality come from?",
                            "Will there be 'Virtual Date!' updates?",
                            "What software was used to create 'Virtual Date!'?",
                            "Behind."
                            ],

                    "labels":
                            [
                            "0",
                            "1",
                            "2",
                            "3",
                            "4",
                            "5",
                            "6",
                            "7",
                            "8",
                            "9",
                            "10",
                            "11",
                            "12",
                            "13"
                            ]
                    }

question_labels_es = {
                    
                    "0": 
                        [
                        ["neutral2", "Bueno...", "normal", None],
                        ["normal", "Según mis datos de personaje, tengo 19 años.", "normal", None],
                        ["happy", "Así que soy legalmente mayor de edad.", "excuse", None],
                        ["normal", "Aunque espero que tengas mínimo 18 años.", "excuse", None],
                        ["jeje", "No por nada malo.", "normal", None],
                        ["normal", "Pero creo que este tipo de juegos no es para que un menor de edad lo juegue.", "excuse", None],
                        ["jeje", "No quiero meterme en problemas.", "normal", None],
                        ["jeje", "", "normal", "exp:5"]
                        ],
                    
                    "1": 
                        [
                        ["neutral2", "Bueno...", "normal", None],
                        ["neutral", "Eso no lo se.", "normal", None],
                        ["normal", "Ya que por mi nombre seguro pensaras que soy japonesa.", "date", None],
                        ["normal", "Pero mis datos de personaje no dicen de qué país soy.", "normal", None],
                        ["happy", "Pero tú puedes pensar que soy japonesa o que soy de tú país.", "normal", None],
                        ["happy", "'Ostia tío, has flipao, ¿eh?'", "excuse", None],
                        ["jeje", "Espera, eso es de España.", "normal", None],
                        ["happy", "Jeje.", "normal", None],
                        ["happy", "", "normal", "exp:5"]
                        ],

                    "2": 
                        [
                        ["normal", "Bueno, me mide 30 cm.", "normal", None],
                        ["jeje", "Perdón solo era una broma que queria hacer.", "excuse", None],
                        ["normal", "Ya enserio mido 1.72 m.", "normal", None],
                        ["happy", "Así que soy bastante alta.", "normal", None],
                        ["normal", "Y tú, ¿Cuánto mides?", "normal", None],
                        ["normal", "", "normal", "exp:5"]
                        ],
                    "3": 
                        [
                        ["normal", "¿Si me gusta?", "normal", None],
                        ["happy", "Me encanta.", "normal", None],
                        ["jeje", "Claro, no soy una fan obsesiva del anime.", "normal", None],
                        ["normal", "Pero si me encanta.", "normal", None],
                        ["happy", "Muchas historias interesantes y animaciones increibles.", "excuse", None],
                        ["angry2", "A veces no sé porque piensan que los amantes del anime son personas inadaptadas.", "normal", None],
                        ["angry2", "Si, a muchos nos gusta es por las historias interesantes que tienen o por otra cosa.", "normal", None],
                        ["normal", "Pero si ponemos de ejemplo a la animación estadounidense, usualmente encontraremos contenido infantil.", "excuse", None],
                        ["neutral", "Que obviamente a un adolescente le parecerá extraño ver.", "excuse", None],
                        ["normal", "Por lo que muchos terminamos viendo un anime y así nos comienza a gustar.", "excuse", None],
                        ["jeje", "Claro, no estoy diciendo que los estadounidenses no hagan animaciones increíbles.", "normal", None],
                        ["normal", "Pero creo que estarías de acuerdo en que muchos vemos más anime que series de animación estadounidense.", "normal", None],
                        ["happy", "¿Tú que crees?", "normal", None],
                        ["happy", "", "normal", "exp:5"]
                        ],
                    "4": 
                        [
                        ["normal", "Creo que seguro ya debes saber porque me gusta el anime.", "normal", None],
                        ["normal", "Aunque la verdad no tengo uno favorito.", "date", None],
                        ["jeje", "Todos me gustan.", "normal", None],
                        ["normal", "Pero si tengo que poner uno seria 'Kobayashi-san no Maid Dragon'.", "excuse", None],
                        ["happy", "Su historia me gusta mucho y la animación me parece genial.", "excuse", None],
                        ["normal", "Aunque también me gustan otros como: 'Komi-san Can't Communicate', 'Kaguya-sama Love is War', 'Ijiranaide, Nagatoro-san' y 'Kono Subarashii Sekai ni Shukufuku wo!'", "date", None],
                        ["happy", "Y muchos más.", "normal", None],
                        ["happy", "¿Y Cuales son tus favoritos?", "normal", None],
                        ["happy", "", "normal", "exp:5"]
                        ],
                    "5": 
                        [
                        ["happy", "Claro que me gustan los videojuegos.", "normal", None],
                        ["normal", "No hablo de los videojuegos actualmente populares.", "normal", None],
                        ["normal", "Como Free-Fire o Fortnite o ¿Halo?", "normal", None],
                        ["normal", "Me gustan más los juegos a los que las personas ponen más amor que dinero.", "normal", None],
                        ["jeje", "Aunque a veces no es así.", "normal", None],
                        ["normal", "Es decir, juego menos queridos por los 'Gamers'.", "normal", None],
                        ["normal", "Yo soy más amante de juegos como: 'Five Nights at Freddy's', 'Geometry Dash', 'Friday Night Funkin'', 'Doki Doki Literature Club!' y 'Katawa Shoujo'.", "excuse", None],
                        ["normal", "Y otros más.", "excuse", None],
                        ["jeje", "Sí, la verdad no juego muchos videojuegos.", "excuse", None],
                        ["happy", "Aunque también me gusta 'Minecraft'.", "date", None],
                        ["normal", "Aunque siento que el ya no es como antes.", "normal", None],
                        ["normal", "Pero bueno, no vengo a hablar de eso.", "normal", None],
                        ["normal", "Y dime...", "normal", None],
                        ["happy", "¿Qué videojuegos te gustan?", "excuse", None],
                        ["normal", "", "normal", "exp:5"]
                        ],
                    "6": 
                        [
                        ["happy", "Claro que me gusta.", "normal", None],
                        ["happy", "Mis géneros musicales favoritos son la electrónica y sus derivados.", "excuse", None],
                        ["normal", "Como el Future Bass, el Dubstep, el electro Swing, el Glicth Hop, el Mid Tempo, el House, el Progressive House.", "date", None],
                        ["happy", "Y otros más.", "date", None],
                        ["normal", "Dime, ¿Conocías la existencia de esos géneros musicales?", "excuse", None],
                        ["happy", "Soy muy moderna, jeje.", "normal", None],
                        ["normal", "", "normal", "exp:5"]
                        ],
                    "7": 
                        [
                        ["normal", "Qué bueno que lo preguntas.", "normal", None],
                        ["happy", "Mis artistas favoritos son: Alan Walker, TheFatRat, Marsmellow, Martin Garrix, Kygo, Avicci y David Guetta.", "date", None],
                        ["normal", "Y otros más.", "normal", None],
                        ["normal", "Pero esos son los más conocidos que son mis favoritos.", "date", None],
                        ["normal", "Entre los que puedes no conocer son: OR30, The Living Tombstone, Axel Johansson, FRANDERMAN123 y Kotori.", "date", None],
                        ["normal", "También me gustan algunas canciones de la banda coreana Everglow y Blankpink.", "excuse", None],
                        ["happy", "¿Y cuáles son los tuyos?", "normal", None],
                        ["normal", "", "normal", "exp:5"]
                        ],
                    "8": 
                        [
                        ["jeje", "Yo la verdad no sé.", "normal", None],
                        ["normal", "Bueno, sé un poco.", "normal", None],
                        ["normal", "El lenguaje de programación que se es Python.", "normal", None],
                        ["happy", "El lenguaje de programación en el que se escribió este juego.", "normal", None],
                        ["normal", "Quiero aprender C++, C#, C, Haxe, Lua, JavaScript, HTML5 y CSS.", "excuse", None],
                        ["happy", "Y hay un lenguaje de programación que proviene de Latinoamérica llamado Latino que también me gustaría aprender.", "date", None],
                        ["normal", "Y volviendo a la pregunta.", "excuse", None],
                        ["jeje", "No soy tan buena programadora en Python.", "excuse", None],
                        ["normal", "Pero estoy aprendiendo para ser muy buena.", "normal", None],
                        ["happy", "Así que no esperes que hackee tu PC.", "normal", None],
                        ["normal", "Por cierto se me hace muy curiosa esa carpeta en tus documentos que pesa 13,6 GB y que se llama 'Tarea'.", "excuse", None],
                        ["jeje", "Es broma la verdad no puedo hackear tu PC.", "excuse", None],
                        ["normal", "", "normal", "exp:5"]
                        ],
                    "9": 
                        [
                        ["normal", "Bueno, eso se puede responder fácilmente.", "normal", None],
                        ["normal", "Pero dejame darte algunos detalles.", "date", None],
                        ["normal", "Antes la idea era hacerlo en 'Love2D' un framework para escribir juegos con el lenguaje de programación Lua.", "date", None],
                        ["jeje", "Pero habían más desventajas que beneficios en 'Love2D'.", "normal", None],
                        ["normal", "El juego se hizo en Pygame porque ya se llevaba un tiempo aprendiendo un poco de Pygame y Python.", "excuse", None],
                        ["normal", "Tampoco se hizo en Ren'Py por motivos de aprendizaje.", "normal", None],
                        ["normal", "Menciono a este último porque Virtual Date! tiene este básico y anti-estético sistema de novela visual que es el que estás viendo.", "excuse", None],
                        ["normal", "Ósea la caja de texto.", "excuse", None],
                        ["normal", "Y Ren'Py sería una opción viable.", "excuse", None],
                        ["normal", "En el tema de conversación Python, puedes ver más explicaciones sobre eso.", "normal", None],
                        ["normal", "El juego puede tener muchos errores por no ser programado por un experto.", "excuse", None],
                        ["jeje", "No es porque este hecho en Pygame.", "excuse", None],
                        ["normal", "", "normal", "exp:5"]
                        ],
                    "10": 
                        [
                        ["normal", "Seguro te habrás dado cuenta que mis gustos, no son los 'normales' para una chica.", "date", None],
                        ["normal", "Mi creador decidió colocar la mayor parte de sus gustos en los míos.", "normal", None],
                        ["normal", "Por eso me gusta la programación y la música electrónica.", "normal", None],
                        ["normal", "Y en cuanto a mi personalidad, eso ya es otra cosa.", "normal", None],
                        ["happy", "Jeje.", "normal", None],
                        ["normal", "Sabes, a veces cuando creamos personajes siempre queremos dejar algo de nosotros en ellos.", "normal", None],
                        ["normal", "Puede ser personalidad, gustos, apariencia y otras cosas de nosotros.", "date", None],
                        ["happy", "Creo que así formamos un lazo fuerte con ellos.", "date", None],
                        ["happy", "Así las ideas pueden fluir más fácilmente.", "date", None],
                        ["happy", "¿No lo crees?", "excuse", None],
                        ["normal", "", "normal", "exp:5"]
                        ],
                    "11": 
                        [
                        ["happy", "Pues claro, si se recibe el apoyo emocional pues claro que habrá más actualizaciones.", "excuse", None],
                        ["happy", "Así que no olvides dejar un comentario de apoyo en donde descargaste el juego.", "excuse", None],
                        ["normal", "¿Me imagino que lo descargaste el juego en la página oficial, verdad?", "normal", None],
                        ["normal", "", "normal", "exp:5"]
                        ],
                    "12": 
                        [
                        ["normal", "Entre los softwares usados están: Python, Pygame, Sublime Text, PyInstaller, LMMS, Audacity, Adobe Flash CS6 y Adobe Photoshop CS6.", "date", None],
                        ["normal", "Todos los softwares son libres a excepción de Sublime Text, Adobe Flash y Photoshop.", "date", None],
                        ["happy", "Estamos intentando demostrar que se puede crear un juego de calidad con solo software libre a excepción de los mencionados.", "excuse", None],
                        ["jeje", "Claro este juego no es de gran calidad.", "excuse", None],
                        ["normal", "", "normal", "exp:5"]
                        ]
                    }

question_labels_en = {
                    
                    "0":
                    [
                    ["neutral2", "So...", "normal", None],
                    ["normal", "According to my character data, I'm 19 years old.", "normal", None],
                    ["happy", "So I am legally of legal age.", "excuse", None],
                    ["normal", "Though I hope you're at least 18 years old.", "excuse", None],
                    ["jeje", "Not for anything bad.", "normal", None],
                    ["normal", "But I think this type of game is not for a minor to play.", "excuse", None],
                    ["jeje", "I don't want to get in trouble.", "normal", None],
                    ["jeje", "", "normal", "exp:5"]
                    ],
                                        
                    "1":
                    [
                    ["neutral2", "So...", "normal", None],
                    ["neutral", "I don't know that.", "normal", None],
                    ["normal", "Since by my name you would surely think I'm Japanese.", "date", None],
                    ["normal", "But my character data doesn't say what country I'm from.", "normal", None],
                    ["happy", "But you may think that I'm Japanese or that I'm from your country.", "normal", None],
                    ["happy", "'Damn man, you freaked out, huh?'", "excuse", None],
                    ["jeje", "Wait, that's from Spain.", "normal", None],
                    ["happy", "Hehe.", "normal", None],
                    ["happy", "", "normal", "exp:5"]
                    ],

                    "2":
                    [
                    ["normal", "Well, it's 30 cm.", "normal", None],
                    ["jeje", "Sorry, that was just a joke I wanted to make.", "excuse", None],
                    ["normal", "I'm really 1.72m already", "normal", None],
                    ["happy", "So I'm pretty tall.", "normal", None],
                    ["normal", "And you, how tall are you?", "normal", None],
                    ["normal", "", "normal", "exp:5"]
                    ],
                    "3":
                    [
                    ["normal", "Do I like it?", "normal", None],
                    ["happy", "I love it.", "normal", None],
                    ["jeje", "Sure, I'm not an obsessive fan of anime.", "average", None],
                    ["normal", "But I love it.", "normal", None],
                    ["happy", "Lots of interesting stories and amazing animations.", "excuse", None],
                    ["angry2", "Sometimes I don't know why they think anime lovers are misfits.", "normal", None],
                    ["angry2", "Yes, many of us like it because of the interesting stories they have or for something else.", "normal", None],
                    ["normal", "But if we take American animation as an example, we will usually find children's content.", "excuse", None],
                    ["neutral", "Which obviously a teenager would find strange to see.", "excuse", None],
                    ["normal", "So many of us end up watching an anime and that's how we start to like it.", "excuse", None],
                    ["jeje", "Sure, I'm not saying Americans don't make amazing animations.", "normal", None],
                    ["average", "But I think you would agree that many of us watch more anime than American animated series.", "average", None],
                    ["happy", "what do you think?", "normal", None],
                    ["happy", "", "normal", "exp:5"]
                    ],
                    "4":
                    [
                    ["normal", "I think you probably already know why I like anime.", "normal", None],
                    ["normal", "Although I don't really have a favorite.", "date", None],
                    ["jeje", "I like them all.", "normal", None],
                    ["normal", "But if I have to put one it would be 'Kobayashi-san no Maid Dragon'.", "excuse", None],
                    ["happy", "I really like your story and I think the animation is great.", "excuse", None],
                    ["average", "Although I also like others like: 'Komi-san Can't Communicate', 'Kaguya-sama Love is War', 'Ijiranaide, Nagatoro-san' and 'Kono Subarashii Sekai ni Shukufuku wo!'" , "date", None],
                    ["happy", "And many more.", "normal", None],
                    ["happy", "And which ones are your favourites?", "normal", None],
                    ["happy", "", "normal", "exp:5"]
                    ],
                    "5":
                    [
                    ["happy", "Of course I like video games.", "normal", None],
                    ["normal", "I'm not talking about currently popular video games.", "normal", None],
                    ["normal", "Like Free-Fire or Fortnite or Halo?", "normal", None],
                    ["normal", "I like games more where people put more love than money into.", "normal", None],
                    ["jeje", "Although sometimes it's not like that.", "normal", None],
                    ["normal", "That is, game less loved by 'Gamers'.", "normal", None],
                    ["normal", "I'm more of a lover of games like: 'Five Nights at Freddy's', 'Geometry Dash', 'Friday Night Funkin'', 'Doki Doki Literature Club!' and 'Katawa Shoujo'.", "excuse", None],
                    ["normal", "And others.", "excuse", None],
                    ["jeje", "Yes, I don't really play many video games.", "excuse", None],
                    ["happy", "Although I like 'Minecraft' too.", "date", None],
                    ["normal", "Although I feel that he is not like before.", "normal", None],
                    ["normal", "But hey, I'm not here to talk about that.", "normal", None],
                    ["normal", "And tell me...", "normal", None],
                    ["happy", "What video games do you like?", "excuse", None],
                    ["normal", "", "normal", "exp:5"]
                    ],
                    "6":
                    [
                    ["happy", "Of course I like it.", "normal", None],
                    ["happy", "My favorite musical genres are electronic and its derivatives.", "excuse", None],
                    ["normal", "Like Future Bass, Dubstep, Electro Swing, Glith Hop, Mid Tempo, House, Progressive House.", "date", None],
                    ["happy", "And others.", "date", None],
                    ["normal", "Tell me, did you know the existence of those musical genres?", "excuse", None],
                    ["happy", "I'm very modern, hehe.", "normal", None],
                    ["normal", "", "normal", "exp:5"]
                    ],
                    "7":
                    [
                    ["normal", "Nice of you asked.", "normal", None],
                    ["happy", "My favorite artists are: Alan Walker, TheFatRat, Marsmellow, Martin Garrix, Kygo, Avicci and David Guetta.", "date", None],
                    ["normal", "And others.", "normal", None],
                    ["normal", "But those are the most popular ones that are my favorites.", "date", None],
                    ["normal", "Among the ones you may not know are: OR30, The Living Tombstone, Axel Johansson, FRANDERMAN123 and Kotori.", "date", None],
                    ["normal", "I also like some songs by the Korean band Everglow and Blankpink.", "excuse", None],
                    ["happy", "And what are yours?", "normal", None],
                    ["normal", "", "normal", "exp:5"]
                    ],
                    "8":
                    [
                    ["jeje", "I really don't know.", "normal", None],
                    ["normal", "Well, I know a little.", "normal", None],
                    ["normal", "The programming language used is Python.", "normal", None],
                    ["happy", "The programming language this game was written in.", "normal", None],
                    ["normal", "I want to learn C++, C#, C, Haxe, Lua, JavaScript, HTML5 and CSS.", "excuse", None],
                    ["happy", "And there is a programming language that comes from Latin America called Latino that I would like to learn too.", "date", None],
                    ["normal", "And going back to the question.", "excuse", None],
                    ["jeje", "I'm not that good of a Python programmer.", "excuse", None],
                    ["normal", "But I'm learning to be very good.", "normal", None],
                    ["happy", "So don't expect me to hack your PC.", "normal", None],
                    ["normal", "By the way, that folder in your documents that weighs 13.6 GB and is called 'Task' is very curious to me.", "excuse", None],
                    ["jeje", "Just kidding, I can't hack your PC.", "excuse", None],
                    ["normal", "", "normal", "exp:5"]
                    ],
                    "9":
                    [
                    ["normal", "Well, that can be easily answered.", "normal", None],
                    ["normal", "But let me give you some details.", "date", None],
                    ["normal", "Before, the idea was to do it in 'Love2D', a framework for writing games with the Lua programming language.", "date", None],
                    ["jeje", "But there were more drawbacks than benefits in 'Love2D'.", "normal", None],
                    ["normal", "The game was made in Pygame because it had already been learning a bit about Pygame and Python for a while.", "excuse", None],
                    ["normal", "Not done in Ren'Py either for learning purposes.", "normal", None],
                    ["normal", "I mention this last one because Virtual Date! has this basic and unsightly visual novel system that you're looking at.", "excuse", None],
                    ["normal", "I mean the text box.", "excuse", None],
                    ["normal", "And Ren'Py would be a viable option.", "excuse", None],
                    ["normal", "In the Python thread, you can see more explanations about that.", "normal", None],
                    ["normal", "The game may have many errors because it was not programmed by an expert.", "excuse", None],
                    ["jeje", "It's not because it's done in Pygame.", "excuse", None],
                    ["normal", "", "normal", "exp:5"]
                    ],
                    "10":
                    [
                    ["normal", "Surely you have noticed that my tastes are not 'normal' for a girl.", "date", None],
                    ["normal", "My creator decided to put most of his tastes in mine.", "normal", None],
                    ["normal", "That's why I like programming and electronic music.", "normal", None],
                    ["normal", "And as for my personality, that's something else.", "normal", None],
                    ["happy", "Hehe.", "normal", None],
                    ["normal", "You know, sometimes when we create characters we always want to leave something of ourselves in them.", "normal", None],
                    ["normal", "It can be personality, tastes, appearance and other things about us.", "date", None],
                    ["happy", "I think that's how we form a strong bond with them.", "date", None],
                    ["happy", "So ideas can flow more easily.", "date", None],
                    ["happy", "Don't you think so?", "excuse", None],
                    ["normal", "", "normal", "exp:5"]
                    ],
                    "eleven":
                    [
                    ["happy", "Of course, if emotional support is received, of course there will be more updates.", "excuse", None],
                    ["happy", "So don't forget to leave a supportive comment where you downloaded the game.", "excuse", None],
                    ["normal", "I assume you downloaded the game from the official page, right?", "normal", None],
                    ["normal", "", "normal", "exp:5"]
                    ],
                    "12":
                    [
                    ["normal", "Among the software used are: Python, Pygame, Sublime Text, PyInstaller, LMMS, Audacity, Adobe Flash CS6 and Adobe Photoshop CS6.", "date", None],
                    ["normal", "All software is free except Sublime Text, Adobe Flash and Photoshop.", "date", None],
                    ["happy", "We are trying to prove that you can create a quality game with only free software except those mentioned.", "excuse", None],
                    ["jeje", "Of course this game is not of great quality.", "excuse", None],
                    ["normal", "", "normal", "exp:5"]
                    ]
                    }

################
# Me siento... #
################

i_feel_es = {
                
                "types": 
                        [
                        "Feliz.",
                        "Triste.",
                        "Emocionado/a.",
                        "Motivado/a.",
                        "Aburrido/a.",
                        "Agotado/a.",
                        "Enojado/a.",
                        "Desmotivado/a.",
                        "Atrás."
                        ],

                "labels":
                        [
                        "0",
                        "1",
                        "2",
                        "3",
                        "4",
                        "5",
                        "6",
                        "7",
                        "8"
                        ]
            }

i_feel_en = {
                
            "types":
                    [
                    "Happy.",
                    "Sad.",
                    "Excited.",
                    "Motivated.",
                    "Boring.",
                    "Sold out.",
                    "Angry.",
                    "Unmotivated.",
                    "Behind."
                    ],

            "labels":
                    [
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8"
                    ]
            }

feel_labels_es = {

                "0": 
                    [
                    ["happy", "Que bien que estés feliz.", "normal", None],
                    ["normal", "Aún el juego no tiene un menú de selección de 'Si o no', pero espero que estés feliz por algo grande.", "excuse", None],
                    ["happy", "O mejor que estés feliz por algo pequeño.", "excuse", None],
                    ["normal", "Porque no sé si lo sabes, pero las cosas pequeñas dan un poco más de felicidad que las grandes.", "normal", None],
                    ["normal", "Sonara raro pero a veces el llenarnos de sentimientos de felicidad muy grandes, quedaremos en el que las cosas pequeñas no nos darán felicidad.", "excuse", None],
                    ["normal", "Claro, necesitamos sentimientos de felicidad grandes.", "normal", None],
                    ["happy", "Pero creo que el ponernos felices por cosas pequeñas nos hará ver mejor la vida.", "excuse", None],
                    ["normal", "¿No sé si estés de acuerdo?", "normal", None],
                    ["normal", "", "normal", "exp:3"]

                    ],
                "1": 
                    [
                    ["sad2", "¿Por qué estás triste?", "normal", None],
                    ["normal", "Vamos, ¿Por qué lo estarías?", "normal", None],
                    ["happy", "La vida es muy corta para vivirla con tristeza.", "normal", None],
                    ["sad", "Claro, a veces llegan esos momentos en el que nos desmotivamos o pasa algo que nos entristece.", "normal", None],
                    ["normal", "Pero sabias que las personas se pueden poner tristes hasta 3 veces al mes.", "excuse", None],
                    ["happy", "Pero sonríe 20 veces.", "excuse", None],
                    ["normal", "Aunque si estás. Cuando yo estoy triste hago las cosas que me gustan para ya no estarlo.", "date", None],
                    ["normal", "Intenta hacer lo que te gusta para reanimarte.", "excuse", None],
                    ["happy", "Confía en mí ya no estés triste.", "normal", None],
                    ["happy", "", "normal", "exp:3"]
                    ],
                "2": 
                    [
                    ["happy", "Que bien.", "normal", None],
                    ["happy", "Espero que los estés por haber cumplido algo.", "normal", None],
                    ["happy", "O quizás porque estás esperando el estreno de la segunda temporada de tu anime favorito.", "excuse", None],
                    ["happy", "Tantas cosas por la cual nos podemos sentir emocionados.", "normal", None],
                    ["happy", "Yo estoy emocionada porque estés jugando este juego.", "normal", None],
                    ["happy", "Jeje.", "normal", None],
                    ["normal", "", "normal", "exp:3"]
                    ],

                "3": 
                    [
                    ["happy", "Eso es genial.", "normal", None],
                    ["normal", "Espero que tu motivación te sirva para seguir adelante.", "normal", None],
                    ["normal", "Por ejemplo si eres dibujante y no tenías la motivación para dibujar entonces aprovecha que ahora estás motivado.", "normal", None],
                    ["normal", "O si eres productor musical usa esa motivación para crear el siguiente éxito musical.", "normal", None],
                    ["normal", "Sabes...", "normal", None],
                    ["normal", "A veces he escuchado que muchas personas esperan a las llamadas 'Musas de la creatividad'.", "normal", None],
                    ["normal", "Es como una forma de motivación que llega esperando a que la misma llegue.", "normal", None],
                    ["normal", "Pero...", "normal", None],
                    ["normal", "¿Y si nunca llega tú 'Musa'?", "normal", None],
                    ["normal", "¿Estarías dispuesto a esperar 1, 10 o 30 años a que llegue?", "normal", None],
                    ["normal", "Mi motivación llega de la nada, no espero mi motivación, yo la busco.", "normal", None],
                    ["normal", "Así que si tú crees en las 'musas' te recomendaría mejor buscar tu motivación en vez de esperarla.", "normal", None],
                    ["normal", "", "normal", "exp:3"]
                    ],
                "4": 
                    [
                    ["normal", "¿Te estoy aburriendo?", "normal", None],
                    ["sad", "Perdón.", "normal", None],
                    ["normal", "¿Crees que te estoy aburriendo?", "normal", None],
                    ["normal", "Bueno si estás jugando este juego puede ser que no.", "normal", None],
                    ["jeje", "Aunque yo también me aburriría con un juego basado en su mayor parte en solo texto.", "normal", None],
                    ["normal", "Pero está versión del juego es solo un prototipo.", "normal", None],
                    ["normal", "En próximas versiones esperamos colocar más características que mejoren la experiencia.", "date", None],
                    ["happy", "Y hacerlo un poco más entretenido.", "date", None],
                    ["happy", "", "normal", "exp:3"]
                    ],

                "5": 
                    [
                    ["normal", "¿Un día muy duro?", "normal", None],
                    ["happy", "Descuida estoy aquí para darte unos consejos para recuperar energía.", "normal", None],
                    ["normal", "Lo ideal sería primero que tomaras un baño con agua caliente.", "date", None],
                    ["jeje", "Que no esté tan caliente por cierto.", "date", None],
                    ["normal", "El bañarse con agua caliente es algo que ayuda a relajar el cuerpo.", "date", None],
                    ["normal", "Mejora la circulación y eso te ayudara a recuperar energía.", "date", None],
                    ["normal", "Después del baño lo ideal sería recostarte un rato.", "normal", None],
                    ["happy", "No sé si estás jugando este juego recostado en tu cama.", "normal", None],
                    ["normal", "Pero si lo estás quiere decir que este te ayuda a recuperar energías.", "date", None],
                    ["embarrassed", "De una u otra manera.", "date", None],
                    ["happy", "Jeje.", "normal", None],
                    ["happy", "", "normal", "exp:3"]
                    ],
                "6": 
                    [
                    ["angry", "Creo que deberías calmarte.", "normal", None],
                    ["angry", "No querrás cometer un error con ese enojo.", "date", None],
                    ["sad", "Cuando estamos enojados tendremos a hacer o decir cosas de las que después nos arrepentimos.", "date", None],
                    ["normal", "Así que primero te recomiendo calmarte.", "normal", None],
                    ["normal", "Haz algo que usualmente te haga feliz.", "normal", None],
                    ["happy", "Y verás cómo ese enojo se ira.", "normal", None],
                    ["happy", "Quizás jugar este juego te ayude a liberar ese enojo.", "normal", None],
                    ["happy", "", "normal", "exp:3"]
                    ],
                "7": 
                    [
                    ["sad", "A veces estar desmotivados es algo que no podemos evitar.", "normal", None],
                    ["sad", "El hecho de pensar en que si las decisiones que tomamos son correctas o no.", "normal", None],
                    ["sad2", "Puede desmotivarnos un poco.", "normal", None],
                    ["sad", "O hasta podemos terminar abandonando proyectos por la desmotivación.", "normal", None],
                    ["happy", "Pero descuida es un sentimiento pasajero.", "normal", None],
                    ["happy", "Solo tenemos que estar preparados para esos pensamientos desmotivadores y salir rápido de ellos.", "normal", None],
                    ["normal", "", "normal", "exp:3"]
                    ]
                }

feel_labels_en = {

                "0":
                [
                ["happy", "I'm glad you're happy.", "normal", None],
                ["normal", "Still the game doesn't have a 'Yes or No' selection menu, but I hope you're happy about something big.", "excuse", None],
                ["happy", "Or you better be happy about something small.", "excuse", None],
                ["normal", "Because I don't know if you know, but small things bring a little more happiness than big ones.", "normal", None],
                ["normal", "It will sound strange but sometimes filling ourselves with very big feelings of happiness, we will remain in which small things will not give us happiness.", "excuse", None],
                ["normal", "Sure, we need big feelings of happiness.", "normal", None],
                ["happy", "But I think that being happy over small things will make us see life better.", "excuse", None],
                ["normal", "I don't know if you agree?", "normal", None],
                ["normal", "", "normal", "exp:3"]

                ],
                "1":
                [
                ["sad2", "Why are you sad?", "normal", None],
                ["normal", "Come on, why would you be?", "normal", None],
                ["happy", "Life is too short to live sadly.", "normal", None],
                ["sad", "Of course, sometimes there come those moments when we get discouraged or something happens that makes us sad.", "normal", None],
                ["normal", "But did you know that people can get sad up to 3 times a month.", "excuse", None],
                ["happy", "But smile 20 times.", "excuse", None],
                ["normal", "Although you are. When I'm sad I do the things I like to not be sad anymore.", "date", None],
                ["normal", "Try to do what you like to revive yourself.", "excuse", None],
                ["happy", "Trust me don't be sad anymore.", "normal", None],
                ["happy", "", "normal", "exp:3"]
                ],
                "2":
                [
                ["happy", "Great.", "normal", None],
                ["happy", "I hope you are for accomplishing something.", "normal", None],
                ["happy", "Or maybe because you're waiting for the premiere of the second season of your favorite anime.", "excuse", None],
                ["happy", "So many things we can feel excited about.", "normal", None],
                ["happy", "I'm excited that you're playing this game.", "normal", None],
                ["happy", "Hehe.", "normal", None],
                ["normal", "", "normal", "exp:3"]
                ],

                "3":
                [
                ["happy", "That's great.", "normal", None],
                ["normal", "I hope your motivation helps you keep going.", "normal", None],
                ["normal", "For example, if you are a cartoonist and you didn't have the motivation to draw then take advantage of the fact that you are now motivated.", "normal", None],
                ["normal", "Or if you're a music producer use that motivation to create the next hit song.", "normal", None],
                ["normal", "Do you know...", "normal", None],
                ["normal", "Sometimes I've heard that many people wait for the so-called 'Muses of creativity'.", "normal", None],
                ["normal", "It's like a form of motivation that arrives waiting for it to arrive.", "normal", None],
                ["normal", "But...", "normal", None],
                ["normal", "And if your 'Muse' never arrives?", "normal", None],
                ["normal", "Would you be willing to wait 1, 10 or 30 years for it to arrive?", "normal", None],
                ["normal", "My motivation comes from nowhere, I don't wait for my motivation, I look for it.", "normal", None],
                ["normal", "So if you believe in the 'muses' I would recommend looking for your motivation instead of waiting for it.", "normal", None],
                ["normal", "", "normal", "exp:3"]
                ],
                "4":
                [
                ["normal", "Am I boring you?", "normal", None],
                ["sad", "Sorry.", "normal", None],
                ["normal", "Do you think I'm boring you?", "normal", None],
                ["normal", "Well if you're playing this game maybe not.", "normal", None],
                ["jeje", "Though I too would get bored with a mostly text based game.", "normal", None],
                ["normal", "But this version of the game is just a prototype.", "normal", None],
                ["normal", "In future versions we hope to put more features that improve the experience.", "date", None],
                ["happy", "And make it a little more fun.", "date", None],
                ["happy", "", "normal", "exp:3"]
                ],

                "5":
                [
                ["normal", "A very hard day?", "normal", None],
                ["happy", "Don't worry, I'm here to give you some tips to recover energy.", "normal", None],
                ["normal", "Ideally, you should first take a bath with hot water.", "date", None],
                ["jeje", "Not so hot by the way.", "date", None],
                ["normal", "Taking a hot bath is something that helps relax the body.", "date", None],
                ["normal", "It improves circulation and that will help you regain energy.", "date", None],
                ["normal", "After the bath, the ideal thing would be to lie down for a while.", "normal", None],
                ["happy", "I don't know if you're playing this game lying on your bed.", "normal", None],
                ["normal", "But if you are, it means that this helps you recover energy.", "date", None],
                ["embarrassed", "One way or another.", "date", None],
                ["happy", "Hehe.", "normal", None],
                ["happy", "", "normal", "exp:3"]
                ],
                "6":
                [
                ["angry", "I think you should calm down.", "normal", None],
                ["angry", "You don't want to make a mistake with that anger.", "date", None],
                ["sad", "When we are angry we will have to do or say things that we later regret.", "date", None],
                ["normal", "So I recommend you calm down first.", "normal", None],
                ["normal", "Do something that usually makes you happy.", "normal", None],
                ["happy", "And you'll see how that anger will go away.", "normal", None],
                ["happy", "Maybe playing this game will help you release that anger.", "normal", None],
                ["happy", "", "normal", "exp:3"]
                ],
                "7":
                [
                ["sad", "Sometimes being unmotivated is something we can't help.", "normal", None],
                ["sad", "The fact of thinking about whether the decisions we make are correct or not.", "normal", None],
                ["sad2", "Might demotivate us a bit.", "normal", None],
                ["sad", "Or we may even end up abandoning projects due to lack of motivation.", "normal", None],
                ["happy", "But don't worry, it's a passing feeling.", "normal", None],
                ["happy", "We just have to be prepared for those demotivating thoughts and get out of them fast.", "normal", None],
                ["normal", "", "normal", "exp:3"]
                ]
            }

#####################################################
############ Temás de conversación ##################
#####################################################

con_themes_es = {

                "types":
                        [
                        "Arte",
                        "Anime",
                        "Historia...",
                        "Música",
                        "Nosotros",
                        "Python",
                        "Tojiko",
                        "Videojuegos",
                        "Virtual Date!",
                        #"Vida",
                        "Atrás"
                        ],

                "labels":
                        [
                        "0",
                        "1",
                        "2",
                        "3",
                        "4",
                        "5",
                        "6",
                        "7",
                        "8",
                        "9"
                        #"10"
                        ],
                "theme":
                        [
                        "art",
                        "anime",
                        "history",
                        "music",
                        "us",
                        "python",
                        "tojiko",
                        "videogames",
                        "virtual_date"
                        #"life"
                        ]
                }

con_themes_en = {

                "types":
                        [
                        "Art",
                        "Anime",
                        "History...",
                        "Music",
                        "Us",
                        "Python",
                        "Tojiko",
                        "Video game",
                        "Virtual Date!",
                        #"Life",
                        "Behind"
                        ],

                "labels":
                        [
                        "0",
                        "1",
                        "2",
                        "3",
                        "4",
                        "5",
                        "6",
                        "7",
                        "8",
                        "9"
                        #"10"
                        ],
                "theme":
                        [
                        "art",
                        "anime",
                        "history",
                        "music",
                        "us",
                        "python",
                        "tojiko",
                        "videogames",
                        "virtual_date"
                        #"life"
                        ]
                }

######################################
########### Subtemás #################
######################################

## Arte ##

art_subthemes_es = {
                    "themes":
                            [
                            "Dibujo digital vs tradicional.",
                            "¿Qué piensas del arte abstracto?",
                            "¿Todo el mundo puede aprender a dibujar?",
                            "15=Aplicaciones que puedo usar para dibujar.",
                            "20=¿Los tutoriales ayudan a mejorar en el dibujo?",
                            "22=Lo increíble del estilo dibujo japonés."
                            ],

                    "numbers":
                            [
                            "0",
                            "1",
                            "2",
                            "3",
                            "4",
                            "5"
                            ]
                    }

art_subthemes_en = {
                    "themes":
                            [
                            "Digital vs traditional drawing.",
                            "What do you think of abstract art?",
                            "Can everyone learn to draw?",
                            "15=Apps I can use to draw.",
                            "20=Do the tutorials help to improve in drawing?",
                            "22=The incredible of the Japanese drawing style."
                            ],

                    "numbers":
                            [
                            "0",
                            "1",
                            "2",
                            "3",
                            "4",
                            "5"
                            ]
                    }

art_numbers_es = {

                 "0":
                    [
                    ["normal", "Creo que antes de hablar de eso deberíamos saber sus diferencias.", "normal", None],
                    ["normal", "El dibujo digital jamás superara al dibujo tradicional.", "excuse", None],
                    ["normal", "Esto debido a que el dibujo digital es literalmente reciente en comparación con el dibujo tradicional.", "excuse", None],
                    ["normal", "Este existió en la revolución digital o algo así.", "normal", None],
                    ["jeje", "Perdón es que no estoy muy documentada.", "normal", None],
                    ["normal", "Pero realmente el dibujo digital existe desde que las computadoras pasaron de ser simples maquinas empresariales a los computadores personales que tenemos hoy en día.", "date", None],
                    ["normal", "El dibujo tradicional...", "excuse", None],
                    ["happy", "Que lo llamaremos así al dibujo que dibujamos en hojas de papel para diferenciarlo del que hacemos en computadora.", "excuse", None],
                    ["normal", "El dibujo tradicional existe desde hace siglos.", "excuse", None],
                    ["happy", "Por lo que creo que podemos decir que el dibujo digital es solo su copia, jeje.", "date", None],
                    ["happy", "No mentira.", "normal", None],
                    ["normal", "El dibujo tradicional y el dibujo digital son literalmente lo mismo.", "excuse", None],
                    ["normal", "Solo que la diferencia del dibujo tradicional al dibujo digital, el dibujo digital debemos escoger primero un software en donde dibujaremos.", "excuse", None],
                    ["normal", "Adaptarnos a su interfaz y sus herramientas.", "normal", None],
                    ["normal", "Ya que existen muchos software para dibujar unos para novatos y otros para profesionales.", "date", None],
                    ["jeje", "Y no tendrán siempre las mismas herramientas.", "date", None],
                    ["jeje", "Por lo que adaptarte a ellos puede ser difícil o sencillo.", "normal", None],
                    ["happy", "En el dibujo tradicional por su parte solo tenemos que tomar una hoja de papel y lapiz.", "excuse", None],
                    ["happy", "Y plasmar nuestras ideas en él.", "excuse", None],
                    ["embarrassed", "Bueno creo realmente no puedo decir que tipo de dibujo es mejor.", "normal", None],
                    ["embarrassed", "Porque realmente no tuviera sentido decirlo.", "normal", None],
                    ["normal", "Pero hablar de ello es interesante.", "normal", None],
                    ["happy", "De lo que dije puedes sacar tus conclusiones y decir que tipo te es más fácil aprender.", "normal", None],
                    ["normal", "Decir que uno es mejor que realmente es innecesario.", "excuse", None],
                    ["happy", "Jeje.", "normal", None],
                    ["happy", "", "normal", "exp:5"]
                    ],

                 "1":
                    [
                    ["neutral", "Bueno...", "normal", None],
                    ["jeje", "La verdad es algo que no entiendo.", "normal", None],
                    ["normal", "El arte abstracto es algo que muchas personas no entenderían a simple vista.", "normal", None],
                    ["normal", "Hay que analizar detalladamente para ver lo que el autor está contando.", "excuse", None],
                    ["normal", "Hay mucho arte abstracto que cuentas una historia que se ve reflejada en el mismo.", "excuse", None],
                    ["jeje", "La verdad no soy de analizar detalladamente lo que veo.", "excuse", None],
                    ["neutral", "Lo que no me gusta de él, es que normalmente debo ser una persona que conozca realmente lo que es el arte.", "normal", None],
                    ["neutral", "Aunque a veces no es así.", "date", None],
                    ["neutral", "Bueno...", "normal", None],
                    ["normal", "Hay veces en el que cualquier persona puede entender lo que el autor quiere reflejar en su pintura.", "normal", None],
                    ["happy", "¿Por qué estamos hablando de pinturas abstractas, verdad?", "date", None],
                    ["jeje", "Jeje.", "date", None],
                    ["normal", "", "normal", "exp:5"],
                    ],

                 "2":
                    [
                    ["happy", "¡Pues claro!", "normal", None],
                    ["happy", "Cualquiera puede aprender a dibujar.", "excuse", None],
                    ["neutral2", "Claro, muchas personas nacen con una habilidad excepcional al dibujar.", "normal", None],
                    ["normal", "Pero eso no quiere decir que cualquiera no pueda aprender.", "normal", None],
                    ["happy", "De hecho sería bueno que te pongas a aprender si no sabes.", "date", None],
                    ["happy", "Y si sabes, que increíble.", "normal", None],
                    ["normal", "Cualquiera puede dibujar, solo que a veces tenemos el miedo y la desconfianza en nosotros mismos.", "normal", None],
                    ["happy", "¿Tú que piensas?", "normal", None],
                    ["happy", "", "normal", "exp:5"]
                    ],

                 "3":
                    [
                    ["normal", "Cuando hablamos de aplicaciones, nos referimos a las aplicaciones para dibujar de forma digital.", "date", None],
                    ["happy", "Así que déjame decirte las que conozco y algunas que he usado.", "date", None],
                    ["jeje", "No son muchas, jeje.", "date", None],
                    ["normal", "Entre las que conozco son:...", "date", None],
                    ["normal", "Paint Tool Sai...", "normal", None],
                    ["normal", "En una aplicación para dibujar que incluyen una cantidad de herramientas para que los dibujantes novatos o profesionales puedan usar.", "excuse", None],
                    ["happy", "Es muy compacta, pero muy poderosa.", "date", None],
                    ["jeje", "Lamentablemente es de paga por lo que no es una buena opción para muchos.", "date", None],
                    ["normal", "Medibang Pro...", "normal", None],
                    ["normal", "Es una aplicación gratuita especializa en el manga...", "excuse", None],
                    ["happy", "Pero no solo fue creada para eso.", "normal", None],
                    ["normal", "Tiene una gran cantidad de herramientas que te ayudarán en tu dibujo.", "date", None],
                    ["jeje", "No la he usado, solo la he visto.", "normal", None],
                    ["normal", "Adobe Photoshop también te puede servir.", "normal", None],
                    ["happy", "Quizás él no está diseñado para el dibujo, pero muchos lo usan para dibujar.", "normal", None],
                    ["normal", "Adobe Illustrator también sirve, pero obviamente no será tan fácil como en Photoshop.", "excuse", None],
                    ["happy", "De esas que mencione solo uso Photoshop.", "normal", None],
                    ["jeje", "Si te entenderás el cómo se desarrolló este juego sabrás el porqué.", "normal", None],
                    ["normal", "Bueno, aunque te dije solo aplicaciones privativas.", "normal", None],
                    ["happy", "¿Por qué no intentas apoyar al software libre probando estás que te diré?", "excuse", None],
                    ["normal", "GIMP es una aplicación libre y de código abierto, es una alternativa a Photoshop.", "date", None],
                    ["happy", "Por lo que también te puede servir.", "excuse", None],
                    ["jeje", "Claro, te tendrás que adaptar a su interfaz.", "excuse", None],
                    ["happy", "Inkscape es una alternativa libre y de código abierto a Adobe Illustrator.", "normal", None],
                    ["normal", "Aunque también deberás adaptarte a su interfaz y que ambos son programas de edición de gráficos vectoriales.", "normal", None],
                    ["normal", "Pero eso no te lo voy a explicar.", "excuse", None],
                    ["happy", "Por lo que te dejo de tarea investigarlo.", "excuse", None],
                    ["normal", "Pero hablemos de mi aplicación software libre favorita para dibujar.", "normal", None],
                    ["happy", "Krita.", "date", None],
                    ["happy", "Krita es una aplicación libre y de código abierto, muy recomendada para dibujar.", "date", None],
                    ["normal", "Pero eso no es todo, también permite hacer animaciones.", "date", None],
                    ["happy", "Además es una alternativa realmente fuerte de Photoshop y Medibang Pro que son software privativos.", "normal", None],
                    ["jeje", "Por cierto tampoco he logrado usar realmente a Krita...", "date", None],
                    ["normal", "Así que dime...", "normal", None],
                    ["happy", "¿Te gustaría probar estás aplicaciones libres para comenzar a dibujar?", "excuse", None],
                    ["happy", "", "normal", "exp:7"]
                    ],

                 "4":
                    [
                    ["happy", "¡Pues claro!", "normal", None],
                    ["happy", "Con tutoriales se puede aprender a dibujar.", "excuse", None],
                    ["normal", "Te cuento un secreto...", "normal", None],
                    ["happy", "Yo aprendí con tutoriales.", "excuse", None],
                    ["jeje", "Bueno, a dibujar en digital.", "excuse", None],
                    ["jeje", "Antes de intentar dibujar en digital ya yo sabía un poco dibujar tradicionalmente.", "excuse", None],
                    ["normal", "Pero si, los tutoriales te pueden ayudar.", "normal", None],
                    ["happy", "Así que, ¿qué esperas?", "excuse", None],
                    ["happy", "Busca los tutoriales o un curso gratuito de dibujo.", "date", None],
                    ["jeje", "Claro, hay cosas que no se pueden aprender con tutoriales.", "excuse", None],
                    ["happy", "Pero después te darás cuenta cuales son.", "date", None],
                    ["happy", "Jeje.", "normal", None],
                    ["happy", "", "normal", "exp:4"]
                    ],

                 "5":
                    [
                    ["happy", "Es increíble, ¿verdad?", "normal", None],
                    ["normal", "Es el estilo de dibujo japonés es increíble.", "normal", None],
                    ["happy", "Trazos tan delicados, tan finos.", "excuse", None],
                    ["happy", "¡Me encantan!", "normal", None],
                    ["normal", "No lo digo solo porque me gusta el anime.", "normal", None],
                    ["normal", "Si no, porque el estilo de dibujo japonés es un poco complicado de adquirir.", "excuse", None],
                    ["normal", "Ya que no puedes usar los métodos de dibujo convencionales que nos enseñan.", "date", None],
                    ["jeje", "O eso creo.", "date", None],
                    ["normal", "Lo que se, es que no puedes usar cualquier tipo de lápiz.", "normal", None],
                    ["normal", "Hay que usar algunos lápices específicos para ese estilo.", "date", None],
                    ["happy", "Pero lo realmente impresionante de ello, es que intentar aprender ese estilo, nos llevara a aprender también a acercarnos a una cultura rica y hermosa.", "excuse", None],
                    ["happy", "Realmente adoro la cultura japonés.", "normal", None],
                    ["happy", "¡Y su estilo de dibujo por supuesto!", "date", None],
                    ["neutral2", "¿Seré japonesa?", "normal", None],
                    ["neutral2", "¿Y por eso me gusta su cultura?", "normal", None],
                    ["happy", "¡¿Quién sabe?!", "normal", None],
                    ["happy", "¡Jaja!", "normal", None],
                    ["happy", "", "normal", "exp:4"]
                    ]
                 }


art_numbers_en = {

                "0":
                [
                ["normal", "I think before we talk about that we should know their differences.", "normal", None],
                ["normal", "Digital drawing will never surpass traditional drawing.", "excuse", None],
                ["normal", "This is because digital drawing is literally recent compared to traditional drawing.", "excuse", None],
                ["normal", "This existed in the digital revolution or something like that.", "normal", None],
                ["jeje", "Sorry, I'm not well informed.", "normal", None],
                ["normal", "But really, digital drawing has existed since computers went from being simple business machines to the personal computers we have today.", "date", None],
                ["normal", "The traditional drawing...", "excuse", None],
                ["happy", "That we will call the drawing that we draw on sheets of paper that way to differentiate it from the one we do on the computer.", "excuse", None],
                ["normal", "Traditional drawing has been around for centuries.", "excuse", None],
                ["happy", "So I think we can say that the digital drawing is just his copy, hehe.", "date", None],
                ["happy", "No lie.", "normal", None],
                ["normal", "Traditional drawing and digital drawing are literally the same thing.", "excuse", None],
                ["normal", "Only the difference between traditional drawing and digital drawing, digital drawing must first choose a software where we will draw.", "excuse", None],
                ["normal", "Adapt to your interface and tools.", "normal", None],
                ["normal", "Since there are many software to draw some for beginners and others for professionals.", "date", None],
                ["jeje", "And they won't always have the same tools.", "date", None],
                ["jeje", "So adapting to them can be difficult or easy.", "normal", None],
                ["happy", "In the traditional drawing for his part we only have to take a sheet of paper and pencil.", "excuse", None],
                ["happy", "And put our ideas into it.", "excuse", None],
                ["embarrassed", "Well I guess I can't really say which kind of drawing is better.", "normal", None],
                ["embarrassed", "Because there really was no point in saying it.", "normal", None],
                ["normal", "But talking about it is interesting.", "normal", None],
                ["happy", "From what I said you can draw your conclusions and say which type is easier for you to learn.", "normal", None],
                ["normal", "Saying that one is better than really is unnecessary.", "excuse", None],
                ["happy", "Hehe.", "normal", None],
                ["happy", "", "normal", "exp:5"]
                ],

                "1":
                [
                ["neutral", "So...", "normal", None],
                ["jeje", "The truth is something I don't understand.", "normal", None],
                ["normal", "Abstract art is something that many people wouldn't understand with the naked eye.", "normal", None],
                ["normal", "You have to analyze in detail to see what the author is saying.", "excuse", None],
                ["normal", "There is a lot of abstract art that tells a story that is reflected in it.", "excuse", None],
                ["jeje", "I'm not really one to analyze in detail what I see.", "excuse", None],
                ["neutral", "What I don't like about it is that normally I have to be a person who really knows what art is.", "normal", None],
                ["neutral", "Though sometimes it isn't.", "date", None],
                ["neutral", "So...", "normal", None],
                ["normal", "There are times when anyone can understand what the author wants to reflect in his painting.", "normal", None],
                ["happy", "Why are we talking about abstract paintings right?", "date", None],
                ["jeje", "Hehe.", "date", None],
                ["normal", "", "normal", "exp:5"],
                ],

                "2":
                [
                ["happy", "Of course!", "normal", None],
                ["happy", "Anyone can learn to draw.", "excuse", None],
                ["neutral2", "Sure, many people are born with exceptional drawing ability.", "normal", None],
                ["normal", "But that doesn't mean that anyone can't learn.", "normal", None],
                ["happy", "Actually it would be nice if you start learning if you don't know.", "date", None],
                ["happy", "And if you know, how amazing.", "normal", None],
                ["normal", "Anyone can draw, it's just that sometimes we have fear and distrust in ourselves.", "normal", None],
                ["happy", "what do you think?", "normal", None],
                ["happy", "", "normal", "exp:5"]
                ],

                "3":
                [
                ["normal", "When we talk about apps, we mean digital drawing apps.", "date", None],
                ["happy", "So let me tell you the ones I know of and some I've used.", "date", None],
                ["jeje", "Not many, hehe.", "date", None],
                ["normal", "Among the ones I know are:...", "date", None],
                ["normal", "Paint Tool Sai...", "normal", None],
                ["normal", "In a drawing application that includes a number of tools for the novice or professional artist to use.", "excuse", None],
                ["happy", "It's very compact, but very powerful.", "date", None],
                ["jeje", "Unfortunately it is paid so it is not a good option for many.", "date", None],
                ["normal", "Medibang Pro...", "normal", None],
                ["normal", "It's a free application specialized in manga...", "excuse", None],
                ["happy", "But it wasn't just created for that.", "normal", None],
                ["normal", "It has a lot of tools that will help you in your drawing.", "date", None],
                ["jeje", "I haven't used it, I've only seen it.", "normal", None],
                ["normal", "Adobe Photoshop can also work for you.", "normal", None],
                ["happy", "Maybe he's not designed for drawing, but many use him for drawing.", "normal", None],
                ["normal", "Adobe Illustrator works too, but obviously it won't be as easy as in Photoshop.", "excuse", None],
                ["happy", "Of those I mentioned I only use Photoshop.", "normal", None],
                ["jeje", "If you understand how this game was developed you will know why.", "normal", None],
                ["normal", "Well, even though I told you only proprietary apps.", "normal", None],
                ["happy", "Why don't you try to support free software by testing what I'll tell you?", "excuse", None],
                ["normal", "GIMP is a free and open source application, it is an alternative to Photoshop.", "date", None],
                ["happy", "So this can also help you.", "excuse", None],
                ["jeje", "Sure, you'll have to adapt to its interface.", "excuse", None],
                ["happy", "Inkscape is a free and open source alternative to Adobe Illustrator.", "normal", None],
                ["normal", "Although you must also adapt to their interface and that both are vector graphics editing programs.", "normal", None],
                ["normal", "But I'm not going to explain that to you.", "excuse", None],
                ["happy", "So I'll leave it up to you to investigate it.", "excuse", None],
                ["normal", "But let's talk about my favorite free software application for drawing.", "normal", None],
                ["happy", "Krita.", "date", None],
                ["happy", "Krita is a free and open source application, highly recommended for drawing.", "date", None],
                ["normal", "But that's not all, it also allows animations.", "date", None],
                ["happy", "It's also a really strong alternative to Photoshop and Medibang Pro which are proprietary software.", "normal", None],
                ["jeje", "By the way I haven't really managed to use Krita either...", "date", None],
                ["normal", "So tell me...", "normal", None],
                ["happy", "Would you like to try these free apps to start drawing?", "excuse", None],
                ["happy", "", "normal", "exp:7"]
                ],

                "4":
                [
                ["happy", "Of course!", "normal", None],
                ["happy", "With tutorials you can learn to draw.", "excuse", None],
                ["normal", "I'm telling you a secret...", "normal", None],
                ["happy", "I learned with tutorials.", "excuse", None],
                ["jeje", "Well, let's draw digitally.", "excuse", None],
                ["jeje", "Before trying to draw digitally I already knew how to draw traditionally a bit.", "excuse", None],
                ["normal", "But yes, the tutorials can help you.", "normal", None],
                ["happy", "So, what are you waiting for?", "excuse", None],
                ["happy", "Look for tutorials or a free drawing course.", "date", None],
                ["jeje", "Sure, there are things you can't learn with tutorials.", "excuse", None],
                ["happy", "But later you'll find out what they are.", "date", None],
                ["happy", "Hehe.", "normal", None],
                ["happy", "", "normal", "exp:4"]
                ],

                "5":
                [
                ["happy", "It's amazing, isn't it?", "normal", None],
                ["normal", "It's the Japanese drawing style is amazing.", "normal", None],
                ["happy", "Strokes so delicate, so fine.", "excuse", None],
                ["happy", "I love them!", "normal", None],
                ["normal", "I'm not just saying that because I like anime.", "normal", None],
                ["normal", "If not, because the Japanese drawing style is a bit difficult to acquire.", "excuse", None],
                ["normal", "Since you can't use the conventional drawing methods we're taught.", "date", None],
                ["jeje", "Or so I think.", "date", None],
                ["normal", "What I know, is that you can't use any kind of pencil.", "normal", None],
                ["normal", "You have to use some specific pencils for that style.", "date", None],
                ["happy", "But what's really impressive about it is that trying to learn that style will also lead us to learn how to approach a rich and beautiful culture.", "excuse", None],
                ["happy", "I really love Japanese culture.", "normal", None],
                ["happy", "And his drawing style of course!", "date", None],
                ["neutral2", "Am I Japanese?", "normal", None],
                ["neutral2", "So I like your culture?", "normal", None],
                ["happy", "Who knows?!", "normal", None],
                ["happy", "Haha!", "normal", None],
                ["happy", "", "normal", "exp:4"]
                ]
                }

### Anime ###

anime_subthemes_es = {

                    "themes":
                            [
                            "¿Solo para inadaptados?",
                            "10=¿Por qué nos gusta el anime?",
                            "35=Oppais cada vez más grandes, que sigue...",
                            "5=¿Qué es una waifu?",
                            "Animación japonesa vs estadounidense.",
                            "60=El ecchi y el hentai.",
                            "80=Lo malo del anime."
                            ],

                    "numbers":
                            [
                            "0",
                            "1",
                            "2",
                            "3",
                            "4",
                            "5",
                            "6"
                            ]

                    }

anime_subthemes_en = {

                    "themes":
                            [
                            "Only for Misfits?"
                            "10=Why do we like anime?",
                            "35=Oppais getting bigger, what's next...",
                            "5=What is a waifu?",
                            "Japanese vs. American Animation.",
                            "60=The ecchi and the hentai.",
                            "80=The bad thing about anime."
                            ],

                    "numbers":
                            [
                            "0",
                            "1",
                            "2",
                            "3",
                            "4",
                            "5",
                            "6"
                            ]

                    }

anime_numbers_es = {

                 "0":
                    [
                    ["neutral", "No has escuchado por ahí, el de que el anime es solo para adolescentes inadaptados.", "excuse", None],
                    ["neutral", "No lo digo enojada.", "normal", None],
                    ["neutral2", "Pero es algo que a veces escucho.", "normal", None],
                    ["neutral", "Creo que no podemos decir u ofender a las personas que nos gustan el anime.", "normal", None],
                    ["neutral", "Muchos tenemos nuestras razones para que nos guste.", "excuse", None],
                    ["neutral2", "Pero claro, hay muchas personas que son 'raros', y les gusta el anime.", "normal", None],
                    ["neutral", "Y seguro por eso muchos tienen esa visión del anime.", "normal", None],
                    ["deception2", "O también dicen que es algo del diablo.", "normal", None],
                    ["deception2", "¿Enserio?", "normal", None],
                    ["deception2", "¿Por qué dicen eso?", "normal", None],
                    ["normal", "Bueno, creo que la verdad debemos respetar que a todos nos gustan cosas diferentes.", "normal", None],
                    ["normal", "El anime no es malo, solo que debemos apreciar lo bueno que tiene.", "excuse", None],
                    ["jeje", "Y saber que las cosas realmente ficticias mostradas en él, nunca llegaran a ser reales.", "normal", None],
                    ["neutral2", "O si...", "normal", None],
                    ["neutral2", "", "normal", "exp:3"],
                    ],

                 "1":
                    [
                    ["normal", "Bueno, muchos tenemos nuestras razones.", "normal", None],
                    ["normal", "Pero creo que puedes compartir las mías.", "excuse", None],
                    ["happy", "Bueno, el anime me gusta por sus animaciones.", "excuse", None],
                    ["happy", "La calidad de la animación japonesa es increíble.", "normal", None],
                    ["happy", "Me encantaría llegar a aprender ese estilo.", "normal", None],
                    ["jeje", "Claro me tardaría mucho en aprenderlo.", "normal", None],
                    ["normal", "Bueno, también las historias es algo por lo que me gusta.", "excuse", None],
                    ["happy", "Tantas historias increíbles y tantas que hay por escoger.", "date", None],
                    ["jeje", "Y al ser tantas es muy difícil escoger cual ver primero.", "date", None],
                    ["normal", "También me gusta por su variada cantidad de diseños en sus personajes.", "normal", None],
                    ["happy", "Y también las personalidades únicas de los mismos.", "normal", None],
                    ["happy", "Olvide mencionar que las actuaciones de voz de los personajes son increíbles.", "date", None],
                    ["jeje", "Claro, no desearas que tus padres escuchen eso.", "date", None],
                    ["normal", "Mis razones realmente son más amplias.", "normal", None],
                    ["happy", "O realmente puedo decir que no hay una razón de porque me gusta el anime.", "normal", None],
                    ["happy", "A veces las cosas que nos gustan de verdad son realmente difícil decir las razones del porque nos gusta.", "excuse", None],
                    ["happy", "Y a ti...", "normal", None],
                    ["happy", "¿Por qué te gusta el anime?", "excuse", None],
                    ["jeje", "Si te gusta, claro.", "excuse", None],
                    ["jeje", "", "excuse", "exp:3"]
                    ],
                 "2":
                    [
                    ["embarrassed", "Me da mucha pena preguntarte...", "normal", None],
                    ["embarrassed", "¿Pero sabes que son las Oppais?", "normal", None],
                    ["normal", "Si ya sabes que igual tengo que explicarlo, y si no lo sabes...", "excuse", None],
                    ["happy", "Entonces escucha atentamente.", "date", None],
                    ["normal", "Las oppais o...", "date", None],
                    ["jeje", "Pechos o...", "normal", None],
                    ["jeje", "Se...", "normal", None],
                    ["happy", "Es la palabra japonesa para referirse a esa parte específica del cuerpo de nosotras las chicas.", "excuse", None],
                    ["jeje", "Obviamente en japonés.", "normal", None],
                    ["normal", "Pero vamos a hablar de su tamaño, pero directamente en el anime.", "normal", None],
                    ["normal", "Muchos ya debemos saber que en el anime, podemos encontrar a muchas chicas con Oppais que usualmente superan el tamaño común y que a pesar de todo en la vida real hay con 'Oppais' cuyo tamaño es fuera de lo común.", "date", None],
                    ["neutral2", "Que el tamaño a veces poco común puede terminar generando muchas polémicas al creador del anime, específicamente del manga.", "normal", None],
                    ["normal", "La que yo conozco es la polémica del tamaño 'exagerado' del pecho de Hana Usaki del manga Usaki-chan wa Asobitai!", "date", None],
                    ["neutral", "Por lo que muchas personas en internet intentaron de una u otra forma hacer que el creador del manga, lo 'terminara' por así decirlo.", "normal", None],
                    ["neutral2", "Ya que la polémica fue tan grande que muchas personas 'rediseñaron' a Usaki-chan con menos pecho y con un poco más de peso que el diseño del autor.", "normal", None],
                    ["neutral", "Pero eso hizo que muchas chicas se sintieron 'discriminadas'...", "normal", None],
                    ["neutral2", "Creo que más bien seria que se sintieron ofendidas e invisibilizadas.", "normal", None],
                    ["normal", "Pero una cosplayer tuvo la valentía de demostrar que en la vida real si hay chicas con 'Oppais' de tamaños pocos comunes.", "excuse", None],
                    ["normal", "Y si existen, solo que son poco comunes.", "excuse", None],
                    ["jeje", "Solo que no veras a una chica esbelta, los pechos son acumulación de grasa por lo que la chica con un tamaño de pecho poco común será un poco rellenita.", "excuse", None],
                    ["neutral2", "Bueno, eso es lo que yo sé.", "normal", None],
                    ["normal", "Pero realmente algo característico del anime es eso, el hecho de que sus personajes femeninos tienen 'oppais' cuyo tamaño es poco común.", "date", None],
                    ["jeje", "Pero en el anime hentai claro que son irrealistas.", "date", None],
                    ["normal", "", "normal", "exp:3"]
                    ],

                 "3":
                    [
                    ["normal", "Si no lo sabes te lo voy a explicar y si lo sabes, ¿Qué crees?", "excuse", None],
                    ["happy", "También lo voy a explicar.", "excuse", None],
                    ["normal", "Una Waifu o 'esposa' es un personaje femenino al que tú le tienes mucho aprecio.", "date", None],
                    ["jeje", "Para decirlo de ese modo.", "date", None],
                    ["jeje", "Ya que el termino real es un personaje femenino al que quieres como tu esposa.", "excuse", None],
                    ["jeje", "Más común de un anime.", "normal", None],
                    ["neutral2", "Y prefiero decir mi termino porque la verdad es poco 'raro' querer como esposa a un personaje que no existe en la vida real.", "normal", None],
                    ["neutral2", "Y muchas personas pudieran decirte loco o loca por eso.", "normal", None],
                    ["normal", "Así que prefiero decir que es un personaje femenino al que le tienes mucho pero mucho aprecio.", "normal", None],
                    ["happy", "Aunque también existe su contraparte masculina, que es un Husbando", "date", None],
                    ["normal", "Pero dime...", "normal", None],
                    ["happy", "¿Soy tu waifu?", "excuse", None],
                    ["happy", "", "normal", "exp:2"]
                    ],
                 "4":
                    [
                    ["normal", "La animación japonesa sabemos que es de una calidad increíble.", "normal", None],
                    ["normal", "Pero la animación estadounidense también.", "excuse", None],
                    ["normal", "Asi que cual podemos decir que es mejor.", "normal", None],
                    ["happy", "Creo que no lo podemos decir.", "normal", None],
                    ["normal", "La animación japonesa o como comunmente la conocemos...", "excuse", None],
                    ["happy", "Anime.", "excuse", None],
                    ["normal", "Tiene sus fuertes.", "normal", None],
                    ["jeje", "Pero la animación estadounidense también.", "normal", None],
                    ["normal", "Las diferencias entre ellas es que la animación es más dirigida al publico infantil.", "excuse", None],
                    ["neutral", "Y la verdad, si es cierto.", "excuse", None],
                    ["normal", "Pero la animación japonesa no se limita al publico infantil.", "normal", None],
                    ["happy", "Por lo que muchos adolescente terminarian viendo anime por eso.", "normal", None],
                    ["normal", "Pero realmente la animación estadounidense puede terminar creando una animación identica a un anime.", "normal", None],
                    ["happy", "Y hacernos creer que es un anime.", "normal", None],
                    ["normal", "Pero realmente un anime es solo aquel que sale de Japón.", "normal", None],
                    ["jeje", "Asi que lamentablemente no podemos llamar anime a una animación parecida al estilo de la animación japonesa hecha en un lugar del mundo que no es japón.", "normal", None],
                    ["neutral2", "¿O si?", "normal", None],
                    ["normal", "", "normal", "exp:3"],
                    ],
                 "5":
                    [
                    ["normal", "Creo que hablar de eso sería un poco extraño.", "normal", None],
                    ["normal", "Así que si tienes a un niño cerca o eres menor de edad será mejor que no escuches.", "normal", None],
                    ["jeje", "Mejor dicho, leas.", "normal", None],
                    ["normal", "Pero bueno...", "normal", None],
                    ["normal", "Si ya has visto muchos animes o leído muchos mangas, sabrás que todos ellos siempre tienen algo por lo que son llamativos.", "excuse", None],
                    ["happy", "O mejor dicho, cada anime o manga tienen sus géneros.", "excuse", None],
                    ["normal", "Que esos mismos géneros determinaran lo que ocurrirá en el.", "normal", None],
                    ["happy", "Que si habrá escenas de acción, escenas o románticas, escenas cómicas o...", "date", None],
                    ["embarrassed", "Escenas subidas de tono.", "normal", None],
                    ["normal", "Que esas mismas son determinadas por los generos 'Ecchi' y 'Hentai'.", "normal", None],
                    ["normal", "El hentai como comúnmente se le conoce al anime +18.", "normal", None],
                    ["jeje", "En que tiene escenas de se...", "normal", None],
                    ["normal", "Pero algo que seguro puedes no saber es que al hentai en Japón no es así.", "normal", None],
                    ["normal", "En Japón se le conoce a ese género como 'Juhachi-kin'.", "date", None],
                    ["normal", "Pero no se le conoce como 'hentai'.", "normal", None],
                    ["normal", "Ya que 'hentai' es la palabra japonesa que significa 'pervertido o pervertida'.", "date", None],
                    ["normal", "El hentai es un género de anime y manga que presenta escenas subidas, extremadamente de tono.", "normal", None],
                    ["normal", "Las historias de los mismos usualmente abarcan lo que son las 'Parafilias' o gustos 'extraños' de las personas.", "excuse", None],
                    ["jeje", "Si, me da mucha pena hablar de eso.", "normal", None],
                    ["normal", "Por eso en el hentai podemos encontrar literalmente todo tipo de cosas.", "normal", None],
                    ["jeje", "Y por eso él no es transmitido por televisión haya en Japón, y usualmente lo encontraremos en DVD o como descarga digital.", "normal", None],
                    ["normal", "Normalmente en formato de OVA's.", "normal", None],
                    ["normal", "O basadas en un manga del mismo género.", "excuse", None],
                    ["normal", "Que pueden tener una historia o simplemente ser una animación de 1, 2, 3 o 4 capítulos.", "normal", None],
                    ["jeje", "Y en el hentai obviamente no se respetan lógicas.", "excuse", None],
                    ["jeje", "Pueden haber pechos exageradamente enormes, tanto que son irreales.", "excuse", None],
                    ["jeje", "También pueden haber gustos o cosas que en la vida real no se respetan o no se aceptan.", "normal", None],
                    ["normal", "Bueno, el ecchi por su parte es un subgénero del hentai.", "date", None],
                    ["jeje", "O eso creo.", "date", None],
                    ["normal", "Ya que en él, hay situaciones subidas de tono pero si llegar a 'eso'.", "normal", None],
                    ["jeje", "Creo que debes de saber a qué me refiero.", "normal", None],
                    ["normal", "Ese tipo de escenas en el ecchi, se llaman 'fanservice'.", "normal", None],
                    ["normal", "En el fanservice subidas de tono si llegar a 'eso'.", "normal", None],
                    ["normal", "Normalmente en el ecchi esas escenas son dirigidas a los personajes femeninos.", "normal", None],
                    ["jeje", "Por razones más reales que simples perversión.", "normal", None],
                    ["normal", "Esas escenas pueden ser ver a una chica semi-desnuda, con traje de baño, con pechos enormes o que los mismos rebotan exageradamente.", "normal", None],
                    ["jeje", "Me meterán en problemas si sigo hablando de esto.", "normal", None],
                    ["jeje", "Así ya entiendes de lo que hablo.", "normal", None],
                    ["jeje", "", "normal", "exp:5"],
                    ],
                 "6":
                    [
                    ["neutral", "Algo que no me gusta del anime, es el hecho en el que muchos fans se vuelven obsesivos.", "normal", None],
                    ["neutral2", "O creen que los personajes de los mismos son reales.", "normal", None],
                    ["neutral2", "Al punto de volverse literalmente loco.", "normal", None],
                    ["neutral2", "Bueno...", "normal", None],
                    ["neutral2", "Es algo que no puedo confirmar.", "normal", None],
                    ["normal", "Pero esa es una de las cosas que no me gusta del anime.", "normal", None],
                    ["neutral", "Otra cosa que no me gusta es el hecho de que la industria del anime está muriendo.", "normal", None],
                    ["neutral2", "Amigo, las industrias tienen que pagar enormes cantidades de dinero al autor del manga.", "normal", None],
                    ["neutral", "Porque el anime es en su mayor parte es la animación de un manga.", "normal", None],
                    ["neutral", "Y esto hace que las industrias ganen literalmente nada por animar esas obras no originales.", "normal", None],
                    ["neutral2", "Ya que si una empresa animadora, hace un anime original, nadie le presta atención.", "normal", None],
                    ["deception", "¿Cómo es eso posible?", "normal", None],
                    ["normal", "Sabes, si las industrias de anime comenzaran a ampliaran sus horizontes y comenzaran a ver historias externas de Japón seria increíble.", "normal", None],
                    ["happy", "Así se afianzaría el intercambio cultural y la industria del anime no moriría.", "normal", None],
                    ["neutral2", "Al menos que ya hayan hecho eso y no funciono.", "normal", None],
                    ["normal", "Pero esa es solo mi opinión.", "normal", None],
                    ["happy", "¿Tú que piensas?", "excuse", None],
                    ["normal", "", "normal", "exp:4"],
                    ],
                }

anime_numbers_en = {

                    "0":
                    [
                    ["neutral", "You haven't heard that anime is only for misfit teenagers.", "excuse", None],
                    ["neutral", "I don't mean it angry.", "normal", None],
                    ["neutral2", "But it's something I sometimes hear.", "normal", None],
                    ["neutral", "I think we can't say or offend people that we like anime.", "normal", None],
                    ["neutral", "Many of us have our reasons for liking it.", "excuse", None],
                    ["neutral2", "But of course, there are many people who are 'weird', and they like anime.", "normal", None],
                    ["neutral", "And that's probably why many have that vision of anime.", "normal", None],
                    ["deception2", "Or they also say it's something from the devil.", "normal", None],
                    ["deception2", "Really?", "normal", None],
                    ["deception2", "Why do they say that?", "normal", None],
                    ["normal", "Well, I think we should really respect that we all like different things.", "normal", None],
                    ["normal", "Anime is not bad, we just have to appreciate how good it is.", "excuse", None],
                    ["jeje", "And to know that the really fictional things shown in it, will never become real.", "normal", None],
                    ["neutral2", "Or if...", "normal", None],
                    ["neutral2", "", "normal", "exp:3"],
                    ],

                    "1":
                    [
                    ["normal", "Well, many of us have our reasons.", "normal", None],
                    ["normal", "But I think you can share mine.", "excuse", None],
                    ["happy", "Well, I like anime for its animations.", "excuse", None],
                    ["happy", "Japanese animation quality is amazing.", "normal", None],
                    ["happy", "I'd love to get to learn that style.", "normal", None],
                    ["jeje", "Of course it would take me a long time to learn it.", "normal", None],
                    ["normal", "Well, the stories are also something I like.", "excuse", None],
                    ["happy", "So many amazing stories and so many to choose from.", "date", None],
                    ["jeje", "And since there are so many it is very difficult to choose which one to see first.", "date", None],
                    ["normal", "I also like it for its varied amount of character designs.", "normal", None],
                    ["happy", "And also their unique personalities.", "normal", None],
                    ["happy", "I forgot to mention that the character voice acting is amazing.", "date", None],
                    ["jeje", "Sure, you wouldn't want your parents to hear that.", "date", None],
                    ["normal", "My reasons really are broader.", "normal", None],
                    ["happy", "Or can I really say that there is no reason why I like anime.", "normal", None],
                    ["happy", "Sometimes the things we really like are really hard to tell the reasons why we like it.", "excuse", None],
                    ["happy", "And you...", "normal", None],
                    ["happy", "Why do you like anime?", "excuse", None],
                    ["jeje", "If you like it, sure.", "excuse", None],
                    ["jeje", "", "excuse", "exp:3"]
                    ],
                    
                    "2":
                    [
                    ["embarrassed", "I'm really sorry to ask you...", "normal", None],
                    ["embarrassed", "But do you know what Oppais are?", "normal", None],
                    ["normal", "If you already know that I still have to explain it, and if you don't know...", "excuse", None],
                    ["happy", "Then listen carefully.", "date", None],
                    ["normal", "The oppais or...", "date", None],
                    ["jeje", "Breasts or...", "normal", None],
                    ["jeje", "I know...", "normal", None],
                    ["happy", "It's the Japanese word to refer to that specific part of the body of us girls.", "excuse", None],
                    ["jeje", "Obviously in Japanese.", "normal", None],
                    ["normal", "But let's talk about its size, but directly in the anime.", "normal", None],
                    ["normal", "Many of us must already know that in the anime, we can find many girls with Oppais that are usually larger than the common size and that despite everything in real life there are 'Oppais' whose size is out of the ordinary .", "date", None],
                    ["neutral2", "That the sometimes unusual size can end up generating a lot of controversy for the creator of the anime, specifically the manga.", "normal", None],
                    ["normal", "The one I know of is the controversy over the 'exaggerated' size of Hana Usaki's chest from the manga Usaki-chan wa Asobitai!", "date", None],
                    ["neutral", "So many people on the internet tried in one way or another to get the creator of the manga to 'end' it so to speak.", "normal", None],
                    ["neutral2", "Since the controversy was so big that many people 'redesigned' Usaki-chan with less chest and a little more weight than the author's design.", "normal", None],
                    ["neutral", "But that made a lot of girls feel 'discriminated'...", "normal", None],
                    ["neutral2", "I think it would rather be that they felt offended and made invisible.", "normal", None],
                    ["normal", "But a cosplayer had the courage to show that in real life there are girls with 'Oppais' of unusual sizes.", "excuse", None],
                    ["normal", "And if they exist, only that they are rare.", "excuse", None],
                    ["jeje", "Only you won't see a slender girl, breasts are accumulation of fat so the girl with unusual breast size will be a bit plump.", "excuse", None],
                    ["neutral2", "Well, that's what I know.", "normal", None],
                    ["normal", "But really something characteristic of the anime is that, the fact that its female characters have 'oppais' whose size is unusual.", "date", None],
                    ["jeje", "But in hentai anime of course they are unrealistic.", "date", None],
                    ["normal", "", "normal", "exp:3"]
                    ],

                    "3":
                    [
                    ["normal", "If you don't know, I'll explain it to you and if you do, what do you think?", "excuse", None],
                    ["happy", "I'll explain it too.", "excuse", None],
                    ["normal", "A Waifu or 'wife' is a female character that you are very fond of.", "date", None],
                    ["jeje", "To put it that way.", "date", None],
                    ["jeje", "Since the actual term is a female character that you want as your wife.", "excuse", None],
                    ["jeje", "Most common in an anime.", "normal", None],
                    ["neutral2", "And I prefer to say my term because it's actually a bit 'weird' to want a character who doesn't exist in real life as your wife.", "normal", None],
                    ["neutral2", "And many people might call you crazy for that.", "normal", None],
                    ["normal", "So I prefer to say that she is a female character that you really, really appreciate.", "normal", None],
                    ["happy", "Although there is also its male counterpart, which is a Husbando", "date", None],
                    ["normal", "But tell me...", "normal", None],
                    ["happy", "Am I your waifu?", "excuse", None],
                    ["happy", "", "normal", "exp:2"]
                    ],
                    "4":
                    [
                    ["normal", "Japanese animation we know is of incredible quality.", "normal", None],
                    ["normal", "But American animation too.", "excuse", None],
                    ["normal", "So which one can we say is better.", "normal", None],
                    ["happy", "I guess we can't tell.", "normal", None],
                    ["normal", "Japanese animation or as we commonly know it...", "excuse", None],
                    ["happy", "Anime.", "excuse", None],
                    ["normal", "It has its strengths.", "normal", None],
                    ["jeje", "But American animation too.", "normal", None],
                    ["normal", "The differences between them is that the animation is more aimed at children," "excuse", None],
                    ["neutral", "And the truth, if true.", "excuse", None],
                    ["normal", "But Japanese animation is not limited to children's audiences.", "normal", None],
                    ["happy", "So many teenagers would end up watching anime because of that.", "normal", None],
                    ["normal", "But actually American animation can end up creating an animation identical to an anime.", "normal", None],
                    ["happy", "And make us believe it's an anime.", "normal", None],
                    ["normal", "But really an anime is only one that comes out of Japan.", "normal", None],
                    ["jeje", "So unfortunately we can't call anime an animation similar to Japanese style animation made in a part of the world that is not Japan.", "normal", None],
                    ["neutral2", "Or if?", "normal", None],
                    ["normal", "", "normal", "exp:3"],
                    ],
                    "5":
                    [
                    ["normal", "I think talking about that would be a bit strange.", "normal", None],
                    ["normal", "So if you have a child around or you're underage you better not listen.", "normal", None],
                    ["jeje", "Rather read.", "normal", None],
                    ["normal", "But well...", "normal", None],
                    ["normal", "If you've already watched many animes or read many mangas, you'll know that all of them always have something that makes them stand out.", "excuse", None],
                    ["happy", "Or rather, each anime or manga has its genres.", "excuse", None],
                    ["normal", "Let those same genres determine what will happen in it.", "normal", None],
                    ["happy", "If there will be action scenes, romantic or scenes, funny scenes or...", "date", None],
                    ["embarrased", "Rusty scenes.", "normal", None],
                    ["normal", "That these are determined by the genres 'Ecchi' and 'Hentai'.", "normal", None],
                    ["normal", "Hentai as anime is commonly known as +18.", "normal", None],
                    ["jeje", "In which he has scenes of se...", "normal", None],
                    ["normal", "But something you probably don't know is that hentai in Japan isn't like that.", "normal", None],
                    ["normal", "In Japan that genre is known as 'Juhachi-kin'.", "date", None],
                    ["normal", "But it's not known as 'hentai'.", "normal", None],
                    ["normal", "Since 'hentai' is the Japanese word for 'perverted'.", "date", None],
                    ["normal", "Hentai is a genre of anime and manga that features risqué scenes, extremely in tone.", "normal", None],
                    ["normal", "Their stories usually cover what are the 'Paraphilias' or 'strange' tastes of people.", "excuse", None],
                    ["jeje", "Yes, I'm very embarrassed to talk about it.", "normal", None],
                    ["normal", "That's why in hentai we can literally find all kinds of things.", "normal", None],
                    ["jeje", "And that's why he's not broadcast on TV there in Japan, and we'll usually find him on DVD or as a digital download.", "normal", None],
                    ["normal", "Usually in OVA format.", "normal", None],
                    ["normal", "Or based on a manga of the same genre.", "excuse", None],
                    ["normal", "That can have a story or just be an animation of 1, 2, 3 or 4 chapters.", "normal", None],
                    ["jeje", "And in hentai obviously logic is not respected.", "excuse", None],
                    ["jeje", "There can be exaggeratedly huge breasts, so much so that they are unreal.", "excuse", None],
                    ["jeje", "There may also be tastes or things that are not respected or accepted in real life.", "normal", None],
                    ["normal", "Well, ecchi for its part is a subgenre of hentai.", "date", None],
                    ["jeje", "Or so I think.", "date", None],
                    ["normal", "Since in it, there are risqué situations but it doesn't get to 'that'.", "normal", None],
                    ["jeje", "I think you should know what I mean.", "normal", None],
                    ["normal", "Those kinds of scenes in ecchi are called 'fanservice'.", "normal", None],
                    ["normal", "In the fanservice it's loud if it gets to 'that'.", "normal", None],
                    ["normal", "Normally in ecchi those scenes are aimed at female characters.", "normal", None],
                    ["jeje", "For more real reasons than simple perversion.", "normal", None],
                    ["normal", "Those scenes can be seeing a girl half-naked, in a bathing suit, with huge breasts or bouncing exaggeratedly.", "normal", None],
                    ["jeje", "I'll get in trouble if I keep talking about this.", "normal", None],
                    ["jeje", "So you understand what I'm talking about.", "normal", None],
                    ["jeje", "", "normal", "exp:5"],
                    ],
                    "6":
                    [
                    ["neutral", "Something I don't like about anime, is the fact that many fans become obsessive about it.", "normal", None],
                    ["neutral2", "Or they think the characters in them are real.", "normal", None],
                    ["neutral2", "To the point of going literally crazy.", "normal", None],
                    ["neutral2", "So...", "normal", None],
                    ["neutral2", "It's something I can't confirm.", "normal", None],
                    ["normal", "But that's one of the things I don't like about anime.", "normal", None],
                    ["neutral", "Another thing I don't like is the fact that the anime industry is dying.", "normal", None],
                    ["neutral2", "Dude, the industries have to pay huge amounts of money to the manga author.", "normal", None],
                    ["neutral", "Because anime is mostly manga animation.", "normal", None],
                    ["neutral", "And this makes industries earn literally nothing for animating those non-original works.", "normal", None],
                    ["neutral2", "Because if an animation company makes an original anime, nobody pays attention to it.", "normal", None],
                    ["deception", "How is that possible?", "normal", None],
                    ["normal", "You know, if the anime industries started to broaden their horizons and start looking at outside stories from Japan that would be amazing.", "normal", None],
                    ["happy", "This would strengthen cultural exchange and the anime industry would not die.", "normal", None],
                    ["neutral2", "Unless they already did that and it didn't work.", "normal", None],
                    ["normal", "But that's just my opinion.", "normal", None],
                    ["happy", "what do you think?", "excuse", None],
                    ["normal", "", "normal", "exp:4"],
                    ],
                    }

## Historias...

history_subthemes_es = {

                        "themes":
                                [
                                "Hachikō: El perro fiel.",
                                "3 barcos."
                                ],

                        "numbers":
                                [
                                "0",
                                "1",
                                "2"
                                ]
                        }

history_subthemes_en = {

                        "themes":
                                [
                                "Hachikō: The faithful dog.",
                                "3 ships."
                                ],

                        "numbers":
                                [
                                "0",
                                "1",
                                "2"
                                ]
                        }

history_numbers_es = {

                    "0": 
                    [
                    ["normal", "Está historia que te voy a contar es real y paso por halla en 1935 en Japón.", "normal", None],
                    ["happy", "Si ya la conoces, que bien.", "excuse", None],
                    ["normal", "Bueno, comencemos.", "normal", None],
                    ["normal", "Todo comienza en 1924, cuando Hachikō fue encontrado por el profesor Hidesaburō Ueno, quien al principio no quería adoptarlo.", "date", None],
                    ["normal", "Pero su hija adolescente insistió, pero Hachikō le causaba al profesor malos recuerdos debido a la muerte de una perra anterior.", "normal", None],
                    ["normal", "Pero termino adoptándolo.", "date", None],
                    ["normal", "Hachikō fue enviado en una caja desde la prefectura de Akita hasta la estación de Shibuya...", "normal", None],
                    ["normal", "Que fue un viaje de dos días en un vagón de equipaje.", "date", None],
                    ["normal", "Pero cuando los sirvientes del profesor fueron a recogerlo, creyeron que estaba muerto.", "normal", None],
                    ["happy", "Cuando llegaron a la casa del profesor, este le acerco una fuente de leche y este se reanimo.", "excuse", None],
                    ["normal", "El profesor lo recogió en su regazo y noto que Hachikō tenía las patas delanteras leventemente desviadas y por eso decidió llamarlo 'Hachi'.", "normal", None],
                    ["happy", "Que significa ocho en japonés, por la similitud con el Kanji para representar el número ocho.", "excuse", None],
                    ["normal", "La hija del profesor dejo la casa de su padre tras quedar embarazada y casarse e irse a vivir a la casa paterna de su esposo.", "normal", None],
                    ["happy", "El profesor pensó en regalar a Hachi, pero termino encariñándose con él.", "excuse", None],
                    ["normal", "Hachi acompañaba al profesor todos los días a la estación Shibuya para despedirse de él todos los días cuando el profesor iba al trabajo.", "normal", None],
                    ["happy", "Y al final del día, Hachi volvía a la estación para recibirlo.", "normal", None],
                    ["normal", "Esa rutina paso a formar parte de las vidas de los dos y no pasó inadvertida por las personas que transitaban ese por el lugar ni por los dueños de los comercios alrededor.", "excuse", None],
                    ["normal", "Esa rutina continuo sin interrupciones hasta el 21 de mayo de 1925...", "excuse", None],
                    ["sad", "Cuando el profesor sufrió una hemorragia cerebral mientras daba una clase en la universidad de Tokio.", "normal", "play:Sad.ogg"],
                    ["sad", "Esa tarde Hachikō corrió a la estación a esperar a su amo.", "normal", None],
                    ["sad2", "Sin embargo, este no llego.", "normal", None],
                    ["sad", "Esa noche Hachikō no regreso a su casa...", "normal", None],
                    ["sad", "Varias veces la familia del profesor intento llevarse a Hachikō de la estación.", "normal", None],
                    ["sad", "Pero este se escapaba y regresaba a la estación a esperar la llegada de su amo.", "normal", None],
                    ["jeje", "Hachikō comenzó a llamar la atención de propios y extraños en la estación.", "excuse", None],
                    ["sad", "Muchas personas fueron testigos de cómo Hachikō acompañaba cada día al profesor antes de su muerte.", "normal", None],
                    ["jeje", "Y fueron esas mismas personas las que se encargaron de cuidarlo y alimentarlo.", "excuse", None],
                    ["embarrassed", "La devoción de Hachikō por su amo fallecido conmovió a los que lo rodeaban, y estos lo apodaron 'El perro fiel'.", "normal", None],
                    ["happy", "En abril de 1934 una estatua de bronce fue erigida en su honor en la estación Shibuya, y el propio Hachikō estuvo presente.", "normal", None],
                    ["sad", "Muchas personas fueron testigos de cómo Hachikō acompañaba cada dia al profesor antes de su muerte.", "normal", None],
                    ["sad", "El 8 de marzo de 1935, 9 años después de la muerte del profesor...", "normal", None],  
                    ["sad2", "Hachikō fue encontrado muerto frente a la estación de Shibuya, tras esperar infructuosamente a su amo casi diez años de la muerte del mismo.", "normal", None],   
                    ["sad", "....", "normal", None],
                    ["embarrassed", "....", "normal", "stop_music"],
                    ["embarrassed", "Sabes...", "normal", None],
                    ["sad3", "Está historia siempre me da tristeza.", "normal", None],
                    ["sad3", "Y a la vez me da un sentimiento de felicidad enorme.", "normal", None],
                    ["embarrassed", "El hecho de que Hachikō haya tenido tanto aprecio por su amo, demuestra lo fiel que puede ser un perro.", "normal", None],
                    ["jeje", "Y eso me hace muy feliz.", "normal", None],
                    ["sad3", "Porque eso demuestra que los perros no son solo mascotas.", "normal", None],
                    ["sad3", "Son nuestros amigos.", "normal", None],
                    ["sad3", "Y parte de la familia.", "normal", None],
                    ["happy", "...", "normal", "no_talk"],
                    ["normal", "Espero que te haya gustado.", "normal", f"play:{config.game_music_default}"],
                    ["sad3", "La historia de Hachikō sin duda es una historia realmente hermosa.", "normal", None],
                    ["jeje", "Algún día me gustaría ir a su estatua haya en la estación de Shibuya.", "normal", None],
                    ["jeje", "", "normal", "exp:8"]
                    ],

                    "1": 
                    [
                    ["normal", "Está historia que te voy a contar es un poco diferente a lo que hemos estado hablando.", "normal", None],
                    ["normal", "Es una historia de religión, pero es interesante.", "excuse", None],
                    ["happy", "Así que pon atención.", "excuse", None],
                    ["normal", "Un hombre estaba naufrago en el mar, y solo tenía una tabla para no hundirse.", "normal", None],
                    ["normal", "En un momento de desesperación mira al cielo y dice:...", "normal", None],
                    ["normal", "'Dios ayúdame no quiero morir'.", "excuse", None],
                    ["normal", "Pasan unos minutos y a lo lejos el hombre ve un barco acercarse.", "normal", None],
                    ["normal", "Uno de los que estaba a bordo del barco ve al hombre y le dice:", "normal", None],
                    ["normal", "'¡Toma este salvavidas para que te rescatemos!'.", "excuse", None],
                    ["normal", "El hombre en el mar a estos les responde:...", "normal", None],
                    ["normal", "'Descuiden, Dios me ayudara'.", "excuse", None],
                    ["normal", "Ante esto, los tripulantes del barco no decidieron más que retirarse.", "normal", None],
                    ["normal", "Un tiempo después otro barco se acerca al hombre.", "normal", None],
                    ["normal", "Uno de los que estaba a bordo de ese barco ve al hombre y le dice:", "normal", None],
                    ["normal", "'¡Deja que te ayudemos, toma este salvavidas!'.", "excuse", None],
                    ["normal", "El hombre en el mar a estos les responde:...", "normal", None],
                    ["normal", "'Descuiden, Dios me ayudara'.", "excuse", None],
                    ["sad3", "Los hombres del barco no tuvieron otra opción más que retirarse.", "excuse", None],
                    ["sad3", "Pasa otro tiempo y un tercer barco se asoma y se acerca al hombre.", "normal", None],
                    ["sad3", "Unos de los que estaba a bordo del barco vio al hombre y le dice:", "normal", None],
                    ["sad3", "'¡Déjanos ayudarte, toma este salvavidas!'.", "excuse", None],
                    ["sad3", "El hombre en el mar le responde:...", "normal", None],
                    ["sad3", "'Descuiden, Dios me ayudara'.", "excuse", None],
                    ["embarrassed", "Sin otra opción, el barco solo se alejó.", "normal", None],
                    ["sad3", "Pasaron horas y el hombre finalmente termino hundiendose en el mar, agotado.", "excuse", None],
                    ["sad3", "El hombre se ahogó.", "normal", None],
                    ["embarrassed", "Y al llegar al cielo, enojado se acerca a Dios y le dice:...", "normal", None],
                    ["normal", "'¡Dios, ¿por qué no me ayudaste?!'.", "excuse", None],
                    ["normal", "Ante esa pregunta, Dios le responde al hombre:...", "normal", None],
                    ["happy", "'Hijo mío, envié esos tres barcos en tu ayuda'.", "excuse", None],
                    ["happy", "...", "normal", "no_talk"],
                    ["happy", "¿Qué te pareció?", "excuse", None],
                    ["normal", "Está historia a pesar de no formar parte de mis creencias, es una historia interesante.", "normal", None],
                    ["neutral", "Muchos creyentes creen que Dios resolverá sus problemas sin ellos poner de su parte.", "normal", None],
                    ["neutral2", "Pero no es así.", "normal", None],
                    ["sad3", "Está historia refleja que Dios te da los caminos para ayudarte.", "excuse", None],
                    ["sad3", "Pero nosotros decidimos si tomarlos o no.", "excuse", None],
                    ["happy", "Por eso me encanta esta historia.", "normal", None],
                    ["normal", "Ya que cambia todo lo que conocía y creí de la religión.", "normal", None],
                    ["normal", "Dime, si eres creyente...", "normal", None],
                    ["happy", "¿Está historia cambio tu forma de ver la religión?", "excuse", None],
                    ["happy", "", "excuse", "exp:7"]
                    ]
                    }

history_numbers_en = {

                    "0":
                    [
                    ["normal", "This story that I am going to tell you is real and I went through halla in 1935 in Japan.", "normal", None],
                    ["happy", "If you already know her, great.", "excuse", None],
                    ["normal", "Okay, let's get started.", "normal", None],
                    ["normal", "It all starts in 1924, when Hachikō was found by Professor Hidesaburō Ueno, who at first did not want to adopt him.", "date", None],
                    ["normal", "But his teenage daughter insisted, but Hachikō gave the teacher bad memories due to the death of a previous dog.", "normal", None],
                    ["normal", "But I end up adopting it.", "date", None],
                    ["normal", "Hachikō was sent in a box from Akita Prefecture to Shibuya Station...", "normal", None],
                    ["normal", "That was a two-day trip in a baggage car.", "date", None],
                    ["normal", "But when the professor's servants came to pick him up, they thought he was dead.", "normal", None],
                    ["happy", "When they arrived at the teacher's house, he brought him a fountain of milk and he revived.", "excuse", None],
                    ["normal", "The teacher picked it up on his lap and noticed that Hachikō's front legs were slightly deviated and that's why he decided to call it 'Hachi'.", "normal", None],
                    ["happy", "Which means eight in Japanese, due to the similarity with the Kanji to represent the number eight.", "excuse", None],
                    ["normal", "The teacher's daughter left her father's house after getting pregnant and getting married and going to live in her husband's father's house.", "normal", None],
                    ["happy", "The teacher thought of giving Hachi away, but ended up becoming fond of him.", "excuse", None],
                    ["normal", "Hachi accompanied the teacher to Shibuya station every day to say goodbye to him every day when the teacher went to work.", "normal", None],
                    ["happy", "And at the end of the day, Hachi would return to the station to receive it.", "normal", None],
                    ["normal", "This routine became part of the lives of both of them and did not go unnoticed by the people who passed through the place or by the owners of the surrounding shops.", "excuse", None],
                    ["normal", "This routine continued without interruption until May 21, 1925...", "excuse", None],
                    ["sad", "When the professor suffered a brain hemorrhage while teaching a class at the University of Tokyo.", "normal", "play:Sad.ogg"],
                    ["sad", "That afternoon Hachikō ran to the station to wait for his master.", "normal", None],
                    ["sad2", "However, this one didn't arrive.", "normal", None],
                    ["sad", "That night Hachikō didn't return home...", "normal", None],
                    ["sad", "Several times the teacher's family tried to take Hachikō from the station.", "normal", None],
                    ["sad", "But this one escaped and returned to the station to wait for his master's arrival.", "normal", None],
                    ["jeje", "Hachikō began to attract the attention of everyone at the station.", "excuse", None],
                    ["sad", "Many people witnessed how Hachikō accompanied the teacher every day before his death.", "normal", None],
                    ["jeje", "And it was those same people who took care of him and fed him.", "excuse", None],
                    ["embarrassed", "Hachikō's devotion to his deceased master moved those around him, and they nicknamed him 'The Faithful Dog'.", "normal", None],
                    ["happy", "In April 1934 a bronze statue was erected in his honor at Shibuya Station, and Hachikō himself was present.", "normal", None],
                    ["sad", "Many people witnessed how Hachikō accompanied the teacher every day before his death.", "normal", None],
                    ["sad", "March 8, 1935, 9 years after the death of Professor...", "normal", None],
                    ["sad2", "Hachikō was found dead in front of Shibuya station, after waiting unsuccessfully for his master for almost ten years after his death.", "normal", None],
                    ["sad", "....", "normal", None],
                    ["embarrassed", "....", "normal", "stop_music"],
                    ["embarrassed", "You know...", "normal", None],
                    ["sad3", "This story always makes me sad.", "normal", None],
                    ["sad3", "And at the same time it gives me a feeling of enormous happiness.", "normal", None],
                    ["embarrassed", "The fact that Hachikō was so fond of his master shows how faithful a dog can be.", "normal", None],
                    ["jeje", "And that makes me very happy.", "normal", None],
                    ["sad3", "Because that shows that dogs are not just pets.", "normal", None],
                    ["sad3", "They are our friends.", "normal", None],
                    ["sad3", "And part of the family.", "normal", None],
                    ["happy", "...", "normal", "no_talk"],
                    ["normal", "I hope you liked it.", "normal", f"play:{config.game_music_default}"],
                    ["sad3", "Hachikō's story is certainly a really beautiful story.", "normal", None],
                    ["jeje", "Someday I would like to go to his statue there in Shibuya station.", "normal", None],
                    ["jeje", "", "normal", "exp:8"]
                    ],

                    "1":
                    [
                    ["normal", "This story that I am going to tell you is a little different from what we have been talking about.", "normal", None],
                    ["normal", "It's a religious story, but it's interesting.", "excuse", None],
                    ["happy", "So pay attention.", "excuse", None],
                    ["normal", "A man was shipwrecked at sea, and he only had a board to keep from sinking.", "normal", None],
                    ["normal", "In a moment of despair he looks at the sky and says:...", "normal", None],
                    ["normal", "'God help me I don't want to die'.", "excuse", None],
                    ["normal", "A few minutes pass and in the distance the man sees a ship approaching.", "normal", None],
                    ["normal", "One of those who was on board the ship sees the man and says:", "normal", None],
                    ["normal", "'Take this life jacket so we can rescue you!'.", "excuse", None],
                    ["normal", "The man in the sea answers these:...", "normal", None],
                    ["normal", "'Don't worry, God help me'.", "excuse", None],
                    ["normal", "Given this, the ship's crew decided nothing more than to withdraw.", "normal", None],
                    ["normal", "Some time later another ship approaches the man.", "normal", None],
                    ["normal", "One of those who was on board that ship sees the man and says:", "normal", None],
                    ["normal", "'Let us help you, take this life jacket!'.", "excuse", None],
                    ["normal", "The man in the sea answers these:...", "normal", None],
                    ["normal", "'Don't worry, God help me'.", "excuse", None],
                    ["sad3", "The men on the ship had no choice but to retreat.", "excuse", None],
                    ["sad3", "Another time passes and a third ship appears and approaches the man.", "normal", None],
                    ["sad3", "Some of those who were on board the boat saw the man and said:", "normal", None],
                    ["sad3", "'Let us help you, take this life jacket!'.", "excuse", None],
                    ["sad3", "The man in the sea replies:...", "normal", None],
                    ["sad3", "'Don't worry, God help me'.", "excuse", None],
                    ["embarrassed", "With no choice, the ship just moved away.", "normal", None],
                    ["sad3", "Hours passed and the man finally ended up sinking into the sea, exhausted.", "excuse", None],
                    ["sad3", "The man drowned.", "normal", None],
                    ["embarrassed", "And upon reaching heaven, angry he approaches God and says:...", "normal", None],
                    ["normal", "'God, why didn't you help me?!'.", "excuse", None],
                    ["normal", "Given this question, God answers man:...", "normal", None],
                    ["happy", "'My son, I sent those three ships to your aid'.", "excuse", None],
                    ["happy", "...", "normal", "no_talk"],
                    ["happy", "How did you like it?", "excuse", None],
                    ["normal", "This story, despite not being part of my beliefs, is an interesting story.", "normal", None],
                    ["neutral", "Many believers believe that God will solve their problems without them doing their part.", "normal", None],
                    ["neutral2", "But it's not like that.", "normal", None],
                    ["sad3", "This story reflects that God gives you the ways to help you.", "excuse", None],
                    ["sad3", "But we decide whether to take them or not.", "excuse", None],
                    ["happy", "That's why I love this story.", "normal", None],
                    ["normal", "Since it changes everything I knew and believed about religion.", "normal", None],
                    ["normal", "Tell me, if you are a believer...", "normal", None],
                    ["happy", "Did this story change your view of religion?", "excuse", None],
                    ["happy", "", "excuse", "exp:7"]
                    ]
                    }

## Música

music_subthemes_es = {
                    
                    "themes":
                            [
                            "¿Cualquiera puede hacer música?",
                            "Programas para hacer música.",
                            "¿Se puede aprender a hacer música con tutoriales?",
                            "20=Lo increíble de la música",
                            "30=La música en la actualidad",
                            "15=LMMS: Hagamos música de forma libre.",
                            "40=¿Qué piensas de Bad Bunny?"
                            ],

                    "numbers":
                            [
                            "0",
                            "1",
                            "2",
                            "3",
                            "4",
                            "5",
                            "6"
                            ]
                    }

music_subthemes_en = {
                    
                    "themes":
                            [
                            "Can anyone make music?"
                            "Programs to make music.",
                            "Can you learn to make music with tutorials?",
                            "20=The incredible of music",
                            "30=Music Today"
                            "15=LMMS: Let's make music for free.",
                            "40=What do you think of Bad Bunny?"
                            ],

                    "numbers":
                            [
                            "0",
                            "1",
                            "2",
                            "3",
                            "4",
                            "5",
                            "6"
                            ]
                    }

music_numbers_es = {

                    "0":
                    [
                    ["normal", "Claro.", "normal", None],
                    ["happy", "Cualquiera puede.", "normal", None],
                    ["normal", "Con los avances tecnológicos cualquiera puede aprender a hacer música.", "normal", None],
                    ["neutral", "Anteriormente, necesitabas tener un estudio previo para hacer música.", "normal", None],
                    ["neutral2", "Y hablo de que antes que existieran los softwares de producción musical.", "normal", None],
                    ["happy", "Que obviamente vinieron con la era digital.", "date", None],
                    ["neutral", "Aunque actualmente igual necesitamos estudiar un poco sobre música para poder hacerla.", "normal", None],
                    ["normal", "Pero sin duda es mucho más fácil que hace años.", "normal", None],
                    ["happy", "Así que si quieres aprender a hacer música, tienes la oportunidad de hacerlo.", "normal", None],
                    ["normal", "En internet puedes encontrar una infinidad de tutoriales para poder aprender a hacer música.", "excuse", None],
                    ["jeje", "Pero claro deberás escoger el software de producción musical de tu preferencia.", "normal", None],
                    ["normal", "Así que esperas...", "normal", None],
                    ["normal", "Ve a aprender a hacer música.", "normal", None],
                    ["normal", "", "normal", "exp:3"]
                    ],

                    "1":
                    [
                    ["normal", "Bueno, existen una cantidad bastante grande de programas de producción musical.", "normal", None],
                    ["normal", "Pero te hare una lista de solo los que conozco, y me enfatizare en los que uso.", "date", None],
                    ["happy", "Si, también hago música.", "date", None],
                    ["normal", "Entre los programas de producción musical que conozco son:...", "normal", None],
                    ["normal", "Reaper.", "normal", None],
                    ["normal", "Es un programa de producción musical de pago para crear música.", "excuse", None],
                    ["jeje", "Si, varios de los programas que mencionare son de pago y son software privativos.", "excuse", None],
                    ["jeje", "La interfaz de Reaper es más parecida a un editor de audio que un software de producción musical.", "normal", None],
                    ["normal", "Pero se puede hacer música con él.", "normal", None],
                    ["normal", "Reaper está disponible en varias licencias, la gratuita y de pago y puede ser ejecutado en Microsoft Windows, MacOS y Linux.", "normal", None],
                    ["normal", "También tenemos a Logic Pro.", "normal", None],
                    ["neutral2", "Es un software de producción musical también de pago pero a diferencia de los otros que mencionare, este es exclusivamente para MacOS.", "normal", None],
                    ["neutral", "Hasta donde sé.", "normal", None],
                    ["neutral", "Por eso no puedo decir mucho de él.", "normal", None],
                    ["normal", "También tenemos a Cubase.", "normal", None],
                    ["normal", "Un software de producción musical desarrollado por la empresa Steinberg.", "normal", None],
                    ["happy", "La empresa desarrolladora de los conocidos instrumentos VST.", "normal", None],
                    ["normal", "Si apenas estás entrando en el mundo de la producción musical ya prontos sabrás que son.", "excuse", None],
                    ["jeje", "Tampoco conozco mucho de Cubase porque tampoco lo he usado.", "excuse", None],
                    ["normal", "Tenemos al más conocido de todos.", "normal", None],
                    ["happy", "FL Studio.", "normal", None],
                    ["normal", "Es un software de producción musical con el que podemos realizar nuestra propia música a través de una interfaz sencilla y fácil de usar.", "normal", None],
                    ["happy", "Tan popular es que hasta tiene su propia waifu llamada FL-chan.", "normal", None],
                    ["normal", "Cuando busques tutoriales de cómo hacer usualmente encontraras tutoriales con FL Studio.", "normal", None],
                    ["jeje", "Lamentablemente FL Studio es un software de pago y privativo.", "normal", None],
                    ["jeje", "Y la verdad no es muy barato que digamos.", "normal", None],
                    ["normal", "Pero pensemos un poco en el software libre y échale un vistazo a su alternativa libre y de código abierto.", "excuse", None],
                    ["happy", "LMMS.", "normal", None],
                    ["normal", "Es un software de producción musical que al igual que FL Studio nos permite hacer nuestra propia música mediante su interfaz sencilla y fácil de usar.", "normal", None],
                    ["jeje", "LMMS y FL Studio son software muy diferentes por los que no puedes esperar que tengan la misma interfaz.", "normal", None],
                    ["jeje", "Debido a que LMMS es una propuesta libre, actualmente el no cumple con todas las características como FL Studio.", "date", None],
                    ["happy", "Pero que eso no te detenga en querer echarle un ojo.", "normal", None],
                    ["normal", "Bueno, tienes una cantidad un poco pequeña para escoger.", "normal", None],
                    ["normal", "Dime...", "normal", None],
                    ["happy", "¿Con cuál te quedaras?", "excuse", None],
                    ["happy", "", "normal", "exp:4"]
                    ],


                    "2":
                    [
                    ["normal", "Bueno, esa es una pregunta fácil de responder.", "normal", None],
                    ["happy", "Claro que se puede aprender con tutoriales.", "normal", None],
                    ["happy", "Solo tienes que saber dónde buscarlos.", "normal", None],
                    ["normal", "Youtube está repleto de tutoriales de cómo hacer música.", "excuse", None],
                    ["normal", "hay muchas personas que saben mucho y comparten su conocimiento en videos.", "excuse", None],
                    ["jeje", "Claro, para profesionalizarte en producción musical si debes ver un curso en ello", "normal", None],
                    ["normal", "Pero mi respuesta será la misma.", "normal", None],
                    ["happy", "Si se puede aprender con tutoriales.", "normal", None],
                    ["normal", "", "normal", "exp:2"]
                    ],

                    "3":
                    [
                    ["normal", "Sabes, algo que me encanta de la música es lo increíble que es.", "normal", None],
                    ["jeje", "Si, suena un poco tonto sin decir una razón.", "normal", None],
                    ["happy", "La música es algo increíble por su forma en la puede transmitir sentimientos, emociones y contar historias.", "normal", None],
                    ["happy", "El hecho de que los sonidos puedan transmitir sentimientos y emociones es algo emocionante.", "normal", None],
                    ["normal", "Las historias las cuentan en las letras que se escriben para la música.", "normal", None],
                    ["jeje", "Si tiene letra, claro.", "normal", None],
                    ["happy", "Hay muchas historias inspiradoras contadas en músicas.", "normal", None],
                    ["embarrassed", "También historias tristes o melancólicas.", "normal", None],
                    ["neutral2", "Lamentablemente como muchas cosas que existen actualmente...", "normal", None],
                    ["deception", "Fue usada para sobreexplotar a niños que por tener talento para la música sus padres aprovechaban eso.", "normal", None],
                    ["neutral2", "Que años atrás las leyes de protección infantil no eran tan ¿severas?", "normal", None],
                    ["neutral2", "Y los padres podían decidir el futuro de su hijo y lo que iba estudiar sin que este se opusiera.", "normal", None],
                    ["normal", "Pero quitemos eso de lado.", "normal", None],
                    ["jeje", "Ya que no se es correcto.", "normal", None],
                    ["normal", "La música es algo completamente interesante.", "normal", None],
                    ["normal", "Tantos géneros musicales.", "normal", None],
                    ["happy", "Tantos artistas increíbles.", "normal", None],
                    ["happy", "¿Qué más puedo decir?", "normal", None],
                    ["happy", "Es simplemente increíble.", "normal", None],
                    ["normal", "", "normal", "exp:3"]
                    ],

                    "4":
                    [
                    ["neutral2", "Sabes...", "normal", None],
                    ["neutral", "Actualmente la música es algo que muchas personas han cambiado radicalmente.", "normal", None],
                    ["neutral", "Los artistas famosos ya no se esfuerzan en crear música.", "normal", None],
                    ["neutral2", "Y hablo de los artistas de Reggaetón.", "normal", None],
                    ["deception", "Un género musical que actualmente está siendo muy sobreexplotado y muy sobrevalorado.", "normal", None],
                    ["neutral2", "Anteriormente el Reggaetón era un género como cualquier otro.", "normal", None],
                    ["neutral2", "Los artistas se esforzaban al hacer una nueva canción de Reggaetón.", "normal", None],
                    ["neutral", "Claro, el Reggaetón siempre a tratado sobre temas sexuales.", "normal", None],
                    ["angry", "Pero creo que en la actualidad ya muchos ven normal el hecho de los 'artistas' hablen de temas sexuales como si nada en sus 'canciones'.", "normal", None],
                    ["angry2", "Sexualizan a la mujer como si fuese un objeto y apoyan el consumo de drogas.", "normal", None],
                    ["angry", "Y a los oyentes les encanta.", "normal", None],
                    ["deception", "Ni siquiera las chicas se enojan por ser menospreciadas en las letras de las canciones.", "normal", None],
                    ["deception", "¿Hasta dónde hemos llegado?", "normal", None],
                    ["angry", "La música es algo más grande que simplemente una forma de ganar dinero sobreexplotando un género musical dañado.", "normal", None],
                    ["deception", "Pero si sigo hablando me meteré en problemas.", "normal", None],
                    ["deception", "...", "normal", "no_talk"],
                    ["normal", "Bueno, creo que ya se fue el enojo.", "normal", None],
                    ["normal", "", "normal", "exp:2"]
                    ],

                    "5":
                    [
                    ["normal", "Sabes, hay una forma de hacer música de forma libre y gratuita.", "normal", None],
                    ["happy", "Y es con el software de producción musical, LMMS.", "excuse", None],
                    ["normal", "LMMS o Linux Multimedia Studio es un software de producción musical libre y de código abierto.", "normal", None],
                    ["normal", "Creado para ser una alternativa a programas privativos y de corte comercial como FL Studio, Cubase o Logic Pro.", "normal", None],
                    ["normal", "Es un software que está disponible para Microsoft Windows, MacOS y Linux.", "normal", None],
                    ["happy", "Así que si usas Linux puedes usar LMMS y hacer música en él.", "normal", None],
                    ["normal", "Bueno, LMMS es un software muy similar al popular FL Studio.", "normal", None],
                    ["normal", "Su interfaz es muy sencilla por lo que acostumbraras a el rápidamente.", "normal", None],
                    ["jeje", "Si haz usado FL Studio notaras que LMMS no tiene las mismas características que los softwares privativos ya mencionados.", "excuse", None],
                    ["normal", "Pero a pesar de eso, LMMS es muy poderoso.", "normal", None],
                    ["jeje", "Claro, deberás acostumbrarte a sus características faltantes.", "normal", None],
                    ["happy", "Pero que eso no te detenga en querer probarlo.", "normal", None],
                    ["normal", "Porque te voy a decir una frase que escuche por ahí:", "normal", None],
                    ["normal", "'No es el DAW es el productor'.", "excuse", None],
                    ["jeje", "Aunque no he explicado que significa DAW, ¿verdad?", "normal", None],
                    ["normal", "Bueno...", "normal", None],
                    ["normal", "DAW o digital audio workstation son programas que están diseñados para fines relacionados con el sonido.", "normal", None],
                    ["normal", "Ya que no todos los DAW son de producción musical.", "excuse", None],
                    ["jeje", "Pero creo que me estoy saliendo del tema.", "excuse", None],
                    ["normal", "En internet puedes encontrar una cantidad aceptable de tutoriales para poder usar LMMS.", "normal", None],
                    ["normal", "Aunque muchos de FL Studio te servirán para LMMS.", "normal", None],
                    ["happy", "Así que me encantaría que lo probaras.", "normal", None],
                    ["happy", "Apoyemos un poco más al software libre, te aseguro que te encantara.", "normal", None],
                    ["normal", "", "normal", "exp:3"]
                    ],

                    "6":
                    [
                    ["neutral", "Bueno...", "normal", None],
                    ["neutral2", "Sinceramente...", "normal", None],
                    ["neutral2", "Es solo un ejemplo de sobrevaloración.", "normal", None],
                    ["neutral", "La gente lo adora a pesar de que 'canta' horrible y no se le entiende una sola palabra de lo que dice.", "normal", None],
                    ["deception2", "Además que promueve el consumo de drogas y la sexualización de la mujer como un objeto sexual para los hombres.", "normal", None],
                    ["neutral", "Y aun así muchos lo quieren.", "normal", None],
                    ["neutral2", "Espero que no seas un fan del él.", "normal", None],
                    ["neutral", "Yo apoyo que todos tengamos gustos diferentes.", "normal", None],
                    ["neutral2", "Pero no apoyo los gustos por cosas incoherentes y sobrevaloradas.", "normal", None],
                    ["neutral", "Y creo que si sigo diciendo cosas me meteré en problemas.", "normal", None],
                    ["normal", "", "normal", "exp:2"]
                    ]

                    }
                    
music_numbers_en = {

                    "0":
                    [
                    ["normal", "Sure.", "normal", None],
                    ["happy", "Anyone can.", "normal", None],
                    ["normal", "With technological advances anyone can learn to make music.", "normal", None],
                    ["neutral", "Before, you needed to have a previous studio to make music.", "normal", None],
                    ["neutral2", "And I'm talking about before music production software existed.", "normal", None],
                    ["happy", "Which obviously came with the digital age.", "date", None],
                    ["neutral", "Although currently we still need to study a bit about music to be able to make it.", "normal", None],
                    ["normal", "But it's certainly much easier than it was years ago.", "normal", None],
                    ["happy", "So if you want to learn how to make music, you have the chance to do it.", "normal", None],
                    ["normal", "On the internet you can find countless tutorials to learn how to make music.", "excuse", None],
                    ["jeje", "But of course you should choose the music production software of your choice.", "normal", None],
                    ["normal", "So you expect...", "normal", None],
                    ["normal", "Go learn to make music.", "normal", None],
                    ["normal", "", "normal", "exp:3"]
                    ],

                    "1":
                    [
                    ["normal", "Well, there are quite a lot of music production programs out there.", "normal", None],
                    ["normal", "But I'll make you a list of only the ones I know of, and I'll emphasize the ones I use.", "date", None],
                    ["happy", "Yes, I also make music.", "date", None],
                    ["normal", "Among the music production programs I know are:...", "normal", None],
                    ["normal", "Reaper.", "normal", None],
                    ["normal", "It is a paid music production program to create music.", "excuse", None],
                    ["jeje", "Yes, several of the programs that I will mention are paid and are proprietary software.", "excuse", None],
                    ["jeje", "Reaper's interface is more like an audio editor than music production software.", "normal", None],
                    ["normal", "But you can make music with it.", "normal", None],
                    ["normal", "Reaper is available in several licenses, free and paid and can be run on Microsoft Windows, MacOS and Linux.", "normal", None],
                    ["normal", "We also have Logic Pro.", "normal", None],
                    ["neutral2", "It is also paid music production software but unlike the others I will mention, this is exclusively for MacOS.", "normal", None],
                    ["neutral", "As far as I know.", "normal", None],
                    ["neutral", "That's why I can't say much about him.", "normal", None],
                    ["normal", "We also have Cubase.", "normal", None],
                    ["normal", "A music production software developed by the Steinberg company.", "normal", None],
                    ["happy", "The developer of the well-known VST instruments.", "normal", None],
                    ["normal", "If you're just entering the world of music production you'll soon know what they are.", "excuse", None],
                    ["jeje", "I don't know much about Cubase either because I haven't used it either.", "excuse", None],
                    ["normal", "We have the best known of all.", "normal", None],
                    ["happy", "FL Studio.", "normal", None],
                    ["normal", "It is a music production software with which we can make our own music through a simple and easy-to-use interface.", "normal", None],
                    ["happy", "So popular that she even has her own waifu called FL-chan.", "normal", None],
                    ["normal", "When you search for how-to tutorials you will usually find tutorials with FL Studio.", "normal", None],
                    ["jeje", "Unfortunately FL Studio is paid and proprietary software.", "normal", None],
                    ["jeje", "And the truth is not very cheap to say.", "normal", None],
                    ["normal", "But let's think a bit about free software and take a look at its free and open source alternative.", "excuse", None],
                    ["happy", "LMMS.", "normal", None],
                    ["normal", "It is a music production software that, like FL Studio, allows us to make our own music through its simple and easy-to-use interface.", "normal", None],
                    ["jeje", "LMMS and FL Studio are very different software so you can't expect them to have the same interface.", "normal", None],
                    ["jeje", "Because LMMS is a free proposal, currently it does not support all the features like FL Studio.", "date", None],
                    ["happy", "But don't let that stop you from wanting to keep an eye on it.", "normal", None],
                    ["normal", "Well, you have a bit of a small amount to choose from.", "normal", None],
                    ["normal", "Tell me...", "normal", None],
                    ["happy", "Which one will you take?", "excuse", None],
                    ["happy", "", "normal", "exp:4"]
                    ],


                    "2":
                    [
                    ["normal", "Well, that's an easy question to answer.", "normal", None],
                    ["happy", "Of course you can learn with tutorials.", "normal", None],
                    ["happy", "You just have to know where to look for them.", "normal", None],
                    ["normal", "Youtube is full of tutorials on how to make music.", "excuse", None],
                    ["normal", "there are many people who know a lot and share their knowledge in videos.", "excuse", None],
                    ["jeje", "Sure, to professionalize yourself in music production if you must see a course in it", "normal", None],
                    ["normal", "But my answer will be the same.", "normal", None],
                    ["happy", "Yes it can be learned with tutorials.", "normal", None],
                    ["normal", "", "normal", "exp:2"]
                    ],

                    "3":
                    [
                    ["normal", "You know, one thing I love about music is how amazing it is.", "normal", None],
                    ["jeje", "Yeah, it sounds a bit silly without saying a reason.", "normal", None],
                    ["happy", "Music is amazing because of the way it can convey feelings, emotions and tell stories.", "normal", None],
                    ["happy", "The fact that sounds can convey feelings and emotions is something exciting.", "normal", None],
                    ["normal", "The stories are told in the lyrics that are written for the music.", "normal", None],
                    ["jeje", "If it has lyrics, sure.", "normal", None],
                    ["happy", "There are many inspiring stories told in music.", "normal", None],
                    ["embarrassed", "Also sad or melancholic stories.", "normal", None],
                    ["neutral2", "Unfortunately like many things that currently exist...", "normal", None],
                    ["deception", "It was used to overexploit children who, because they had talent for music, their parents took advantage of that.", "normal", None],
                    ["neutral2", "That years ago child protection laws were not so severe?", "normal", None],
                    ["neutral2", "And the parents could decide the future of their son and what he was going to study without his opposition.", "normal", None],
                    ["normal", "But let's get that out of the way.", "normal", None],
                    ["jeje", "Since it is not correct.", "normal", None],
                    ["normal", "The music is something completely interesting.", "normal", None],
                    ["normal", "So many music genres.", "normal", None],
                    ["happy", "So many amazing artists.", "normal", None],
                    ["happy", "what else can I say?", "normal", None],
                    ["happy", "It's just amazing.", "normal", None],
                    ["normal", "", "normal", "exp:3"]
                    ],

                    "4":
                    [
                    ["neutral2", "You know...", "normal", None],
                    ["neutral", "Currently music is something that many people have radically changed.", "normal", None],
                    ["neutral", "Famous artists no longer strive to create music.", "normal", None],
                    ["neutral2", "And I'm talking about Reggaeton artists.", "normal", None],
                    ["deception", "A musical genre that is currently being very overexploited and very overrated.", "normal", None],
                    ["neutral2", "Before, Reggaeton was a genre like any other.", "normal", None],
                    ["neutral2", "The artists were struggling to make a new Reggaeton song.", "normal", None],
                    ["neutral", "Of course, Reggaeton has always dealt with sexual issues.", "normal", None],
                    ["angry", "But I think that nowadays many already see normal the fact that 'artists' talk about sexual issues as if it were nothing in their 'songs'.", "normal", None],
                    ["angry2", "They sexualize women as objects and support drug use.", "normal", None],
                    ["angry", "And listeners love it.", "normal", None],
                    ["deception", "Even girls don't get mad at being put down in song lyrics.", "normal", None],
                    ["deception", "How far have we come?", "normal", None],
                    ["angry", "Music is something bigger than just making money by overexploiting a damaged genre of music.", "normal", None],
                    ["deception", "But if I keep talking I'll get in trouble.", "normal", None],
                    ["deception", "...", "normal", "no_talk"],
                    ["normal", "Well, I think the anger is gone.", "normal", None],
                    ["normal", "", "normal", "exp:2"]
                    ],

                    "5":
                    [
                    ["normal", "You know, there's a way to make music freely and for free.", "normal", None],
                    ["happy", "And it's with music production software, LMMS.", "excuse", None],
                    ["normal", "LMMS or Linux Multimedia Studio is free and open source music production software.", "normal", None],
                    ["normal", "Created to be an alternative to proprietary and commercial programs such as FL Studio, Cubase or Logic Pro.", "normal", None],
                    ["normal", "It is a software that is available for Microsoft Windows, MacOS and Linux.", "normal", None],
                    ["happy", "So if you use Linux you can use LMMS and make music on it.", "normal", None],
                    ["normal", "Well, LMMS is a software very similar to the popular FL Studio.", "normal", None],
                    ["normal", "Its interface is very simple so you will get used to it quickly.", "normal", None],
                    ["jeje", "If you have used FL Studio you will notice that LMMS does not have the same features as the proprietary software already mentioned.", "excuse", None],
                    ["normal", "But despite that, LMMS is very powerful.", "normal", None],
                    ["jeje", "Sure, you'll have to get used to its missing features.", "normal", None],
                    ["happy", "But don't let that stop you from wanting to try it.", "normal", None],
                    ["normal", "Because I am going to tell you a phrase that I hear around:", "normal", None],
                    ["normal", "'It's not the DAW, it's the producer'.", "excuse", None],
                    ["jeje", "Although I haven't explained what DAW means, right?", "normal", None],
                    ["normal", "Well...", "normal", None],
                    ["normal", "DAW or digital audio workstation are programs that are designed for sound-related purposes.", "normal", None],
                    ["normal", "Since not all DAWs are for music production.", "excuse", None],
                    ["jeje", "But I think I'm getting off topic.", "excuse", None],
                    ["normal", "On the internet you can find an acceptable amount of tutorials to be able to use LMMS.", "normal", None],
                    ["normal", "Although many of FL Studio will work for LMMS.", "normal", None],
                    ["happy", "So I'd love for you to try it.", "normal", None],
                    ["happy", "Let's support free software a little more, I assure you that you will love it.", "normal", None],
                    ["normal", "", "normal", "exp:3"]
                    ],

                    "6":
                    [
                    ["neutral", "So...", "normal", None],
                    ["neutral2", "Sincerely...", "normal", None],
                    ["neutral2", "This is just an example of overrating.", "normal", None],
                    ["neutral", "People love him even though he 'sings' horrible and you can't understand a word he says.", "normal", None],
                    ["deception2", "In addition to promoting drug use and the sexualization of women as sexual objects for men.", "normal", None],
                    ["neutral", "And still many want it.", "normal", None],
                    ["neutral2", "I hope you're not a fan of him.", "normal", None],
                    ["neutral", "I support everyone having different tastes.", "normal", None],
                    ["neutral2", "But I don't support liking for inconsistent and overrated stuff.", "normal", None],
                    ["neutral", "And I think if I keep saying things I'll get in trouble.", "normal", None],
                    ["normal", "", "normal", "exp:2"]
                    ]

                    }

# Nosotros

us_subthemes_es = {
                    "themes":
                            [
                            "¿Qué somos?",
                            "30=¿Cuál es el propósito de 'Virtual Date!'?"
                            ],

                    "numbers":
                            [
                            "0",
                            "1"
                            ]
                    }

us_subthemes_en = {
                    "themes":
                            [
                            "What are we?",
                            "30=What is the purpose of 'Virtual Date!'?"
                            ],

                    "numbers":
                            [
                            "0",
                            "1"
                            ]
                    }

us_numbers_es = {

                "0":
                [
                ["neutral2", "Bueno...", "normal", None],
                ["neutral", "Por el título del juego creerás que somos...ya sabes.", "normal", None],
                ["normal", "Pero eso no es así.", "normal", None],
                ["happy", "Ya que las citas no se llaman así por ser exclusivamente de una pareja romántica.", "excuse", None],
                ["happy", "Existen las citas de trabajo, las citas de pareja, las citas de obligación que serían una cita cuyo fin es el ir a un lugar a esperar o hacer algo específico.", "normal", None],
                ["jeje", "O algo así.", "normal", None],
                ["happy", "Y por último....", "normal", None],
                ["happy", "¡Las citas de amigos!", "excuse", None],
                ["normal", "Ya que debido a que el juego no es tan complejo lo mínimo que puedo decir que somos amigos.", "normal", None],
                ["happy", "Eso es lo que somos.", "normal", None],
                ["happy", "", "normal", "exp:2"]
                ],

                "1":
                [
                ["neutral2", "Bueno...", "normal", None],
                ["neutral", "Esa es una pregunta un poco difícil.", "normal", None],
                ["neutral", "Ya que el juego tiene varios propósitos.", "normal", None],
                ["normal", "Uno de ellos es promover el uso de Pygame.", "normal", None],
                ["normal", "Pero si lo que quieres saber es el propósito del juego en si entonces te lo diré.", "excuse", None],
                ["normal", "El propósito del juego es crear una idea del cómo sería tener una relación.", "normal", None],
                ["jeje", "Si, suena un poco tonto.", "normal", None],
                ["normal", "Pero ese es el propósito.", "normal", None],
                ["jeje", "No sé qué te parece.", "normal", None],
                ["jeje", "", "normal", "exp:2"]
                ]
                }

us_numbers_en = {

                "0":
                [
                ["neutral2", "So...", "normal", None],
                ["neutral", "From the game title you'll think we're...you know.", "normal", None],
                ["normal", "But that's not so.", "normal", None],
                ["happy", "Since dates are not called that because they are exclusively for a romantic couple.", "excuse", None],
                ["happy", "There are work dates, couple dates, obligation dates that would be a date whose purpose is to go somewhere to wait or do something specific.", "normal", None],
                ["jeje", "Or something like that.", "normal", None],
                ["happy", "And finally....", "normal", None],
                ["happy", "Friends dating!", "excuse", None],
                ["normal", "Since the game is not that complex, I can say that we are friends at least.", "normal", None],
                ["happy", "That's what we are.", "normal", None],
                ["happy", "", "normal", "exp:2"]
                ],

                "1":
                [
                ["neutral2", "So...", "normal", None],
                ["neutral", "That's a bit of a difficult question.", "normal", None],
                ["neutral", "Since the game has several purposes.", "normal", None],
                ["normal", "One of them is to promote the use of Pygame.", "normal", None],
                ["normal", "But if what you want to know is the purpose of the game itself then I'll tell you.", "excuse", None],
                ["normal", "The purpose of the game is to create an idea of what it would be like to be in a relationship.", "normal", None],
                ["jeje", "Yeah, sounds a bit silly.", "normal", None],
                ["normal", "But that's the purpose.", "normal", None],
                ["jeje", "I don't know what you think.", "normal", None],
                ["jeje", "", "normal", "exp:2"]
                ]
                }

### Python

python_pygame_subthemes_es = {
                                "themes":
                                        [
                                        "¿Juegos complejos en Pygame?",
                                        "¿Por qué 'Virtual Date!' se hizo en Pygame?",
                                        "Ren'Py.",
                                        "30=Python: ¿Solo para novatos?",
                                        "35=Lenguajes interpretados vs compilados."
                                        ],

                                "numbers":
                                        [
                                        "0",
                                        "1",
                                        "2",
                                        "3",
                                        "4"
                                        ]
                            }

python_pygame_subthemes_en = {
                                "themes":
                                        [
                                        "Complex Games in Pygame?",
                                        "Why 'Virtual Date!' was made in Pygame?",
                                        "Ren'Py.",
                                        "30=Python: Only for newbies?",
                                        "35=Interpreted vs Compiled Languages."
                                        ],

                                "numbers":
                                        [
                                        "0",
                                        "1",
                                        "2",
                                        "3",
                                        "4"
                                        ]
                                }

python_pygame_numbers_es = {

                            "0":
                            [
                            ["neutral2", "Bueno...", "normal", None],
                            ["normal", "Con Pygame se pueden hacer juegos complejos.", "normal", None],
                            ["happy", "De hecho estás jugando uno.", "normal", None],
                            ["embarrassed", "Por así decirlo.", "normal", None],
                            ["normal", "Si existen juegos complejos hechos con Pygame.", "normal", None],
                            ["neutral", "Bueno, muchos no les interesa usar Pygame por no contar con una interfaz gráfica.", "normal", None],
                            ["neutral2", "Pygame solo nos provee lo necesario para poder crear un videojuego.", "excuse", None],
                            ["neutral", "El resto de cosas las debemos de crear nosotros.", "normal", None],
                            ["neutral2", "Y creo que por eso muchos no escogerían Pygame en primer lugar.", "normal", None],
                            ["normal", "Los juegos en si son complejos, y Pygame no hace que sean complejos.", "normal", None],
                            ["normal", "La complejidad de los mismos se la damos nosotros.", "excuse", None],
                            ["happy", "Pero claro, Virtual Date! es un poco complejo.", "normal", None],
                            ["jeje", "Claro, muchos juegos son más complejos o extremadamente complejos y más si los hace un experto.", "normal", None],
                            ["normal", "Pero volviendo a la pregunta...", "normal", None],
                            ["normal", "Con Pygame se pueden hacer juegos sencillo y complejos.", "normal", None],
                            ["normal", "Solo debes saber lo que haces.", "normal", None],
                            ["happy", "Y saber usar las funciones de Pygame.", "date", None],
                            ["jeje", "También deberás complementar tu juego con funciones propias.", "date", None],
                            ["normal", "Pero si, si se pueden hacer grandes juegos con Pygame.", "excuse", None],
                            ["jeje", "Creo que simplemente tuve que decir eso, ¿no?", "excuse", None],
                            ["jeje", "", "excuse", "exp:3"]
                            ],

                            "1":
                            [
                            ["normal", "Bueno...", "normal", None],
                            ["normal", "La respuesta puedes haberla ya escuchado.", "excuse", None],
                            ["happy", "Se hizo con Pygame por cuestiones de aprendizaje.", "excuse", None],
                            ["normal", "Pygame al fin y al cabo es Python.", "excuse", None],
                            ["normal", "Por lo que para poder usarlo se necesita tener un conocimiento previo en Python.", "normal", None],
                            ["normal", "Virtual Date! se pudo hacer con Ren'Py.", "normal", None],
                            ["happy", "Qué es un motor de novelas visuales y Virtual Date! contiene un sistema de novela visual.", "normal", None],
                            ["normal", "Pero como dije, no se hizo con Ren'Py por aprender.", "normal", None],
                            ["embarrassed", "Claro, nos pudimos evitar todos los problemas y lo difícil que fue crear está humilde caja de texto.", "normal", None],
                            ["normal", "Pero el ganar conocimiento fue lo que nos motivó a crearlo en Pygame.", "normal", None],
                            ["neutral", "Nos pasó por la mente crearlo con Love2D, pero no sabíamos programar con Lua, y ya teníamos conocimientos previos en Python.", "normal", None],
                            ["jeje", "Claro, este juego no es una obra maestra.", "normal", None],
                            ["happy", "Pero nos sentimos orgullosos del resultado.", "excuse", None],
                            ["jeje", "Tiene sus problemas, es obvio.", "excuse", None],
                            ["normal", "Pero en el futuro puede cambiar.", "normal", None],
                            ["happy", "Hasta puedes ayudarnos a mejorar.", "normal", None],
                            ["happy", "", "normal", "exp:3"]
                            ],

                            "2":
                            [
                            ["normal", "Ren'Py es software para la creación de novelas visuales y simuladores de vida.", "normal", None],
                            ["normal", "Está escrito con Python.", "excuse", None],
                            ["happy", "Y usa Pygame para su funcionamiento.", "excuse", None],
                            ["normal", "Ren'Py actualmente es la primera opción a la hora de crear novelas visuales.", "normal", None],
                            ["normal", "Debido a su sencillo lenguaje de script y a que un usuario que nunca haya tocado o visto Python, puede crear un juego con él.", "excuse", None],
                            ["happy", "Es un software realmente poderoso, y pueden crearse novelas visuales simples a complejas.", "date", None],
                            ["neutral2", "El único problema es que el solo está dirigido a novelas visuales.", "normal", None],
                            ["neutral", "Por lo que si intentamos salir de eso, terminaremos escogiendo otro software.", "normal", None],
                            ["normal", "Pero si lo que quieres es hacer una novela visual, Ren'Py estará allí para ti.", "normal", None],
                            ["normal", "Su documentación te ayudara a familiarizarte con él o también puedes buscar tutoriales en Youtube.", "date", None],
                            ["normal", "El actualmente es una de los mejores software escrito en Python usando Pygame.", "normal", None],
                            ["happy", "Por lo que si no sabías eso, entonces ya lo sabes.", "normal", None],
                            ["normal", "Ren'Py es software libre y de código abierto.", "normal", None],
                            ["normal", "Por lo que si quieres descargarlo solo ve a su página oficial y descargarlo.", "normal", None],
                            ["normal", "Si tienes una PC un poco antigua, la última versión de Ren'Py puede ser que no se ejecute en tu PC.", "date", None],
                            ["happy", "Por lo que usar la versión 7.4.4 te permitirá usar una versión de Ren'Py un poco más cercana a la actual.", "date", None],
                            ["normal", "Te recomiendo usar Linux para aprovechar al máximo el rendimiento de tu PC.", "normal", None],
                            ["normal", "Eso es todo lo que tengo que decir.", "normal", None],
                            ["normal", "", "normal", "exp:3"]
                            ],

                            "3":
                            [
                            ["neutral2", "Algo que he escuchado y es el que Python es solo para novatos.", "normal", None],
                            ["neutral", "Claro, su sintaxis está hecha para que muchos aprendan más rápido que con otros lenguajes de programación.", "normal", None],
                            ["neutral2", "Pero he escuchado que dicen que Python no puede hacer cosas complejas.", "normal", None],
                            ["jeje", "Perdón pero es solo que he escuchado.", "normal", None],
                            ["normal", "Python a pesar de ser un increíble lenguaje el único inconveniente es que al ser un lenguaje de programación de muy alto nivel...", "normal", None],
                            ["jeje", "No puede hacer operaciones con el hardware.", "normal", None],
                            ["normal", "Por lo que para poder crear interfaces graficas necesitas tener un módulo escrito en lenguaje de programación que si pueda hacer operaciones con el hardware.", "normal", None],
                            ["jeje", "Si conoces sobre lenguajes de programación sabrás a lo que me refiero con niveles.", "normal", None],
                            ["normal", "Pero realmente eso no importa, ya que a pesar de eso Python es un lenguaje acto para novatos como para profesionales.", "normal", None],
                            ["happy", "Y de hecho Python en 2022 es uno de los lenguajes de programación más usados.", "normal", None],
                            ["normal", "Por lo que decir que solo novatos lo usan no tuviera sentido.", "normal", None],
                            ["happy", "Así que si quieres entrar en el mundo de la programación; Python te servirá mucho.", "normal", None],
                            ["normal", "", "normal", "exp:3"]
                            ],

                            "4":
                            [
                            ["normal", "Cuando entramos en el mundo de la programación siempre se nos presentara muchos lenguajes de programación para escoger.", "normal", None],
                            ["normal", "Pero ellos siempre están divididos en dos tipos.", "excuse", None],
                            ["normal", "Los lenguajes compilados y los interpretados.", "normal", None],
                            ["normal", "Los Lenguajes de programación compilados son aquellos que antes de la ejecución del programa traducen el código escrito a lenguaje para le la computadora lo pueda entender.", "normal", None],
                            ["normal", "A este archivo creado por el compilador del lenguaje se llama código objeto que después es ejecutado en una fase posterior.", "normal", None],
                            ["normal", "El lenguaje interpretado por su parte lo que hace es ejecutar las ordenes a medida que el programa se va ejecutando.", "date", None],
                            ["normal", "Este interprete se encarga de traducir las ordenes en lenguaje binario o lenguaje de máquina que es el que las computadoras entienden.", "normal", None],
                            ["normal", "Los lenguajes de programación interpretados tienden a consumir un poco más de memoria que los compilados y por ende tienden a ser más lentos.", "normal", None],
                            ["normal", "Un lenguaje de programación compilado tiende a ser 15 a 20 veces más rápido que un lenguaje interpretado.", "normal", None],
                            ["normal", "Pero ellos durante la compilación del código envían error si los hay y no permiten su ejecución hasta que no haya ninguno.", "date", None],
                            ["normal", "Por su parte los interpretados como ya dije ejecutan las ordenes a medida durante su ejecución.", "normal", None],
                            ["normal", "Si hay un error al momento de iniciar el intérprete estos errores mayormente son sintácticos.", "excuse", None],
                            ["normal", "Pero si ocurre cuando el programa está en ejecución se llaman Excepciones.", "normal", None],
                            ["jeje", "Al menos sé que se llaman así en Python.", "normal", None],
                            ["neutral", "Aunque creo que se llama así en otros también.", "normal", None],
                            ["normal", "Algunos ejemplos de lenguajes de programación compilados son:...", "normal", None],
                            ["normal", "C, C++, Haxe y C#.", "excuse", None],
                            ["normal", "Entre los interpretados tenemos a:...", "normal", None],
                            ["normal", "Python, JavaScript y Latino.", "date", None],
                            ["jeje", "Si, hay muchos más lenguajes de programación compilados e interpretados pero esos son los que se.", "date", None],
                            ["normal", "Ningún lenguaje de programación es mejor que otro, ya que no todos pueden cumplir nuestras exigencias.", "normal", None],
                            ["normal", "Pero el que terminemos usando puede ser compilado o interpretado.", "excuse", None],
                            ["normal", "Así que solo hay que escoger cual usar y ya.", "normal", None],
                            ["happy", "Quien sabe, si ya usas un lenguaje de programación puede ser que uses un lenguaje compilado o interpretado.", "normal", None],
                            ["happy", "", "normal", "exp:4"]
                            ]

                            }

python_pygame_numbers_en = {

                            "0":
                            [
                            ["neutral2", "So...", "normal", None],
                            ["normal", "With Pygame you can make complex games.", "normal", None],
                            ["happy", "You are actually playing one.", "normal", None],
                            ["embarrassed", "So to speak.", "normal", None],
                            ["normal", "If there are complex games made with Pygame.", "normal", None],
                            ["neutral", "Well, a lot of people aren't interested in using Pygame because it doesn't have a graphical interface.", "normal", None],
                            ["neutral2", "Pygame only provides us with what is necessary to create a game.", "excuse", None],
                            ["neutral", "The rest of the things we must create ourselves.", "normal", None],
                            ["neutral2", "And I think that's why many wouldn't choose Pygame in the first place.", "normal", None],
                            ["normal", "The games themselves are complex, and Pygame doesn't make them complex.", "normal", None],
                            ["normal", "Their complexity is given by us.", "excuse", None],
                            ["happy", "But of course, Virtual Date! is a bit complex.", "normal", None],
                            ["jeje", "Of course, many games are more complex or extremely complex and more so if they are made by an expert.", "normal", None],
                            ["normal", "But back to the question...", "normal", None],
                            ["normal", "With Pygame you can make simple and complex games.", "normal", None],
                            ["normal", "You just have to know what you're doing.", "normal", None],
                            ["happy", "And know how to use Pygame functions.", "date", None],
                            ["jeje", "You should also complement your game with your own functions.", "date", None],
                            ["normal", "But yes, you can make great games with Pygame.", "excuse", None],
                            ["jeje", "I guess I just had to say that, didn't I?", "excuse", None],
                            ["jeje", "", "excuse", "exp:3"]
                            ],

                            "1":
                            [
                            ["normal", "Well...", "normal", None],
                            ["normal", "You may have already heard the answer.", "excuse", None],
                            ["happy", "Got Pygame for learning purposes.", "excuse", None],
                            ["normal", "Pygame is Python after all.", "excuse", None],
                            ["normal", "So in order to use it you need to have some prior knowledge of Python.", "normal", None],
                            ["normal", "Virtual Date! could be done with Ren'Py.", "normal", None],
                            ["happy", "What is a visual novel engine and Virtual Date! contains a visual novel system.", "normal", None],
                            ["normal", "But like I said, it wasn't done with Ren'Py by learning.", "normal", None],
                            ["embarrassed", "Of course, we could avoid all the problems and how difficult it was to create this humble text box.", "normal", None],
                            ["normal", "But gaining knowledge was what motivated us to create it in Pygame.", "normal", None],
                            ["neutral", "We thought about creating it with Love2D, but we didn't know how to program with Lua, and we already had previous knowledge of Python.", "normal", None],
                            ["jeje", "Of course, this game is not a masterpiece.", "normal", None],
                            ["happy", "But we are proud of the result.", "excuse", None],
                            ["jeje", "It has its problems, it's obvious.", "excuse", None],
                            ["normal", "But in the future it may change.", "normal", None],
                            ["happy", "You can even help us improve.", "normal", None],
                            ["happy", "", "normal", "exp:3"]
                            ],

                            "2":
                            [
                            ["normal", "Ren'Py is software for creating visual novels and life simulators.", "normal", None],
                            ["normal", "It is written with Python.", "excuse", None],
                            ["happy", "And it uses Pygame for its operation.", "excuse", None],
                            ["normal", "Ren'Py is currently the first choice when creating visual novels.", "normal", None],
                            ["normal", "Because of its simple scripting language and a user who has never touched or seen Python before, can create a game with it.", "excuse", None],
                            ["happy", "It's a really powerful software, and can create simple to complex visual novels.", "date", None],
                            ["neutral2", "The only problem is that it's only aimed at visual novels.", "normal", None],
                            ["neutral", "So if we try to get out of that, we'll end up choosing another software.", "normal", None],
                            ["normal", "But if you want to make a visual novel, Ren'Py will be there for you.", "normal", None],
                            ["normal", "Its documentation will help you get familiar with it or you can also look for tutorials on Youtube.", "date", None],
                            ["normal", "This is currently one of the best software written in Python using Pygame.", "normal", None],
                            ["happy", "So if you didn't know that, then you already know.", "normal", None],
                            ["normal", "Ren'Py is free and open source software.", "normal", None],
                            ["normal", "So if you want to download it just go to its official page and download it.", "normal", None],
                            ["normal", "If you have a slightly older PC, the latest version of Ren'Py may not run on your PC.", "date", None],
                            ["happy", "So using version 7.4.4 will allow you to use a version of Ren'Py a bit closer to the current one.", "date", None],
                            ["normal", "I recommend using Linux to get the most out of your PC's performance.", "normal", None],
                            ["normal", "That's all I have to say.", "normal", None],
                            ["normal", "", "normal", "exp:3"]
                            ],

                            "3":
                            [
                            ["neutral2", "Something I've heard is that Python is only for newbies.", "normal", None],
                            ["neutral", "Of course, its syntax is made so that many learn faster than with other programming languages.", "normal", None],
                            ["neutral2", "But I've heard that Python can't do complex things.", "normal", None],
                            ["jeje", "Sorry but that's just what I heard.", "normal", None],
                            ["normal", "Python despite being an incredible language the only drawback is that being a very high level programming language...", "normal", None],
                            ["jeje", "Can't do hardware operations.", "normal", None],
                            ["normal", "So in order to create graphical interfaces you need to have a module written in a programming language that can do operations with the hardware.", "normal", None],
                            ["jeje", "If you know about programming languages you'll know what I mean by levels.", "normal", None],
                            ["normal", "But that doesn't really matter, since Python is still a language suitable for beginners as well as professionals.", "normal", None],
                            ["happy", "And in fact Python in 2022 is one of the most used programming languages.", "normal", None],
                            ["normal", "So saying that only newbies use it wouldn't make sense.", "normal", None],
                            ["happy", "So if you want to get into programming, Python will help you a lot.", "normal", None],
                            ["normal", "", "normal", "exp:3"]
                            ],

                            "4":
                            [
                            ["normal", "When we enter the world of programming we will always be presented with many programming languages to choose from.", "normal", None],
                            ["normal", "But they are always divided into two types.", "excuse", None],
                            ["normal", "Compiled and interpreted languages.", "normal", None],
                            ["normal", "Compiled programming languages are those that before the execution of the program translate the written code into a language that the computer can understand.", "normal", None],
                            ["normal", "This file created by the language compiler is called object code which is then executed at a later stage.", "normal", None],
                            ["normal", "What the interpreted language does is execute the orders as the program is being executed.", "date", None],
                            ["normal", "This interpreter is responsible for translating the commands into binary or machine language which is what computers understand.", "normal", None],
                            ["normal", "Interpreted programming languages tend to consume a bit more memory than compiled languages and therefore tend to be slower.", "normal", None],
                            ["normal", "A compiled programming language tends to be 15 to 20 times faster than an interpreted language.", "normal", None],
                            ["normal", "But during the compilation of the code they send errors if there are any and do not allow their execution until there are none.", "date", None],
                            ["normal", "For their part, the interpreters, as I already said, execute the custom orders during their execution.", "normal", None],
                            ["normal", "If there is an error when starting the interpreter these errors are mostly syntactic.", "excuse", None],
                            ["normal", "But if it occurs when the program is running they are called Exceptions.", "normal", None],
                            ["jeje", "At least I know they're called that in Python.", "normal", None],
                            ["neutral", "Though I think it's called that in others too.", "normal", None],
                            ["normal", "Some examples of compiled programming languages are:...", "normal", None],
                            ["normal", "C, C++, Haxe and C#.", "excuse", None],
                            ["normal", "Among those interpreted we have:...", "normal", None],
                            ["normal", "Python, JavaScript and Latin.", "date", None],
                            ["jeje", "Yes, there are many more compiled and interpreted programming languages but those are the ones I know.", "date", None],
                            ["normal", "No programming language is better than another, since not all of them can meet our requirements.", "normal", None],
                            ["normal", "But the one we end up using can be compiled or interpreted.", "excuse", None],
                            ["normal", "So you just have to choose which one to use and that's it.", "normal", None],
                            ["happy", "Who knows, if you already use a programming language you might use a compiled or interpreted language.", "normal", None],
                            ["happy", "", "normal", "exp:4"]
                            ]

                            }

### Tojiko

tojiko_subthemes_es = {
                        "themes":
                                [
                                "¿Cuándo es tú cumpleaños?",
                                "80=Tu preferencia sexual.",
                                "5=¿Eres una estudiante?",
                                "Boceto.",
                                #"¿Cuáles son tus gustos?",
                                #"¿Solo serás parte de Virtual Date!?",
                                #"Datos de personaje.",
                                ],

                        "numbers":
                                [
                                "0",
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6"
                                ]
                        }

tojiko_subthemes_en = {
                        "themes":
                                [
                                "When is your birthday?",
                                "80=Your sexual preference.",
                                "5=Are you a student?"
                                "Sketch.",
                                #"What do you like?",
                                #"Will you only be a part of Virtual Date!?",
                                #"Character data.",                             
                                ],

                        "numbers":
                                [
                                "0",
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6"
                                ]
                        }

tojiko_numbers_es = {

                    "0":
                    [
                    ["normal", "Mi cumpleaños es el mismo día del lanzamiento del juego.", "normal", None],
                    ["happy", "Así que cada año para poder recordar el lanzamiento del juego.", "normal", None],
                    ["ego", "Así que espero que lo recuerdes.", "normal", None],
                    ["happy", "Un fanart como regalo me encantaría.", "normal", None],
                    ["normal", "", "normal", "exp:2"]
                    ],

                    "1":
                    [
                    ["embarrassed", "Soy un programa de computadora.", "normal", None],
                    ["embarrassed", "No voy a tener una.", "normal", None],
                    ["embarrassed", "Ni siquiera sé si eres chico o chica.", "normal", None],
                    ["normal", "Pero tú puedes hacerte una idea de mi preferencia.", "normal", None],
                    ["happy", "Aunque si tengo una.", "normal", None],
                    ["jeje", "Pero prefiero no decirlo.", "normal", None],
                    ["normal", "", "normal", "exp:2"]
                    ],

                    "2":
                    [
                    ["normal", "Por mi ropa creerás que lo soy.", "normal", None],
                    ["normal", "Pero la verdad es que no.", "normal", None],
                    ["neutral", "No sé ni siquiera sé por qué estoy vestida así.", "normal", None],
                    ["normal", "Pero creo que hay un porque.", "normal", None],
                    ["normal", "Quizás sea porque en los simuladores de citas las chicas usualmente la ven vestidas como estudiante.", "normal", None],
                    ["neutral", "¿O habrá otra razón?", "normal", None],
                    ["normal", "Quien sabe.", "normal", None],
                    ["normal", "", "normal", "exp:2"]
                    ],

                    "3":
                    [
                    ["normal", "Si revisas en la carpeta 'assets' en el directorio del juego.", "normal", None],
                    ["normal", "Encontraras la carpeta 'images'.", "normal", None],
                    ["normal", "Dentro de ella esta una carpeta llamada 'design'.", "date", None],
                    ["normal", "En esa carpeta tienes mi diseño hasta el que estás viendo ahorita.", "normal", None],
                    ["happy", "También podrás descargar el proyecto de mi sprite de forma gratuita.", "date", None],
                    ["normal", "", "normal", "exp:2"]
                    ]
    
                    }

tojiko_numbers_en = {

                    "0":
                    [
                    ["normal", "My birthday is the same day the game is released.", "normal", None],
                    ["happy", "So every year to be able to remember the release of the game.", "normal", None],
                    ["ego", "So I hope you remember.", "normal", None],
                    ["happy", "I would love a fanart as a gift.", "normal", None],
                    ["normal", "", "normal", "exp:2"]
                    ],

                    "1":
                    [
                    ["embarrassed", "I am a computer program.", "normal", None],
                    ["embarrassed", "I won't have one.", "normal", None],
                    ["embarrassed", "I don't even know if you're a boy or a girl.", "normal", None],
                    ["normal", "But you can get an idea of my preference.", "normal", None],
                    ["happy", "Although I do have one.", "normal", None],
                    ["jeje", "But I'd rather not say it.", "normal", None],
                    ["normal", "", "normal", "exp:2"]
                    ],

                    "2":
                    [
                    ["normal", "You'll think I'm normal by my clothes.", "normal", None],
                    ["normal", "But not really.", "normal", None],
                    ["neutral", "I don't even know why I'm dressed like that.", "normal", None],
                    ["normal", "But I think there is a reason.", "normal", None],
                    ["normal", "Maybe it's because in dating sims girls usually see her dressed as a student.", "normal", None],
                    ["neutral", "Or is there another reason?", "normal", None],
                    ["normal", "Who knows.", "normal", None],
                    ["normal", "", "normal", "exp:2"]
                    ],

                    "3":
                    [
                    ["normal", "If you check in the 'assets' folder in the game directory.", "normal", None],
                    ["normal", "You will find the 'images' folder.", "normal", None],
                    ["normal", "Inside it is a folder called 'design'.", "date", None],
                    ["normal", "In that folder you have my design up to the one you are seeing right now.", "normal", None],
                    ["happy", "You can also download my sprite project for free.", "date", None],
                    ["normal", "", "normal", "exp:2"]
                    ]
                        
                    }

### Videojuegos

videogames_subthemes_es = {
                            "themes":
                                    [
                                    "¿Son malos los videojuegos?",
                                    "¿Juegos de código abierto?",
                                    "Novelas visuales y simuladores de citas.",
                                    "50=Doki Doki Literature Club!.",
                                    "55=FNAF: Lleva años existiendo y sigue siendo muy querido.",
                                    "60=¿Cómo puedo hacer mi propio juego?",
                                    "70=Herramientas libres y de código abierto."
                                    ],

                            "numbers":
                                    [
                                    "0",
                                    "1",
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6"
                                    ]
                            }

videogames_subthemes_en = {
                            "themes":
                                    [
                                    "Are video games bad?"
                                    "Open source games?",
                                    "Visual novels and dating sims.",
                                    "50=Doki Doki Literature Club!.",
                                    "55=FNAF: It's been around for years and is still well loved.",
                                    "60=How can I make my own game?",
                                    "70=Free and open source tools."
                                    ],

                            "numbers":
                                    [
                                    "0",
                                    "1",
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6"
                                    ]
                            }

videogames_numbers_es = {

                        "0":
                        [
                        ["neutral2", "Bueno...", "normal", None],
                        ["neutral", "Realmente no.", "normal", None],
                        ["neutral", "Eso es una creencia que muchos padres han promovido.", "normal", None],
                        ["neutral2", "La obsesión por ellos es lo malo.", "normal", None],
                        ["normal", "Pero realmente no son malos.", "normal", None],
                        ["happy", "De hecho ellos tienen muchos beneficios.", "date", None],
                        ["normal", "Entre esos beneficios son el aumento de la concentración.", "normal", None],
                        ["happy", "El jugar videojuegos aumenta la concentración y la mejora la respuesta de toma de decisiones.", "date", None],
                        ["normal", "También estimulan la imaginación.", "normal", None],
                        ["normal", "Y aumenta el aprendizaje del inglés básico.", "normal", None],
                        ["normal", "Debido a que muchos títulos están en inglés.", "normal", None],
                        ["neutral", "Obviamente ellos tienen también sus cosas malas.", "normal", None],
                        ["neutral", "Como la obsesión con ellos que deriva en otros problemas.", "normal", None],
                        ["neutral2", "Como el descuido de tareas importantes.", "excuse", None],
                        ["neutral2", "Agresividad al no permitir el juego.", "normal", None],
                        ["neutral", "Y otro problemas.", "normal", None],
                        ["neutral", "Pero realmente ellos al igual que el uso excesivo de la computadora no causa un daño ocular.", "normal", None],
                        ["neutral2", "Ya que muchos padres han promovido el que los videojuegos dañan la vista.", "excuse", None],
                        ["neutral2", "Pero realmente no es así.", "normal", None],
                        ["neutral2", "Un estudio revelo que los videojuegos al igual que el uso excesivo de la computadora solo causa fatiga visual.", "excuse", None],
                        ["neutral2", "Pero no perderás la vista por ello.", "normal", None],
                        ["neutral", "Hay muchos factores que desencadenan la perdida de la vista.", "normal", None],
                        ["neutral2", "Pero eso no.", "normal", None],
                        ["jeje", "Pero igual no deberías pasar mucho tiempo jugando videojuegos o en frente de un computador.", "normal", None],
                        ["normal", "Pero realmente no son malos.", "normal", None],
                        ["normal", "", "normal", "exp:4"]
                        ],

                        "1":
                        [
                        ["neutral2", "Una pregunta que me he hecho es sobre si los videojuegos de código abierto tendrán un futuro.", "normal", None],
                        ["neutral", "Debido a que las empresas no tienen intenciones de querer liberar los códigos de sus juegos.", "normal", None],
                        ["neutral2", "Y me cruza por la mente de que al parecer esconden algo.", "normal", None],
                        ["normal", "Pero eso no es lo que quiero decir.", "normal", None],
                        ["normal", "Usualmente encontraremos juegos de código abierto cuando son desarrollados independientemente.", "excuse", None],
                        ["jeje", "Ósea que no son desarrollados por una empresa.", "excuse", None],
                        ["normal", "Y algo decir es que hablo de juegos libres cuyo código está disponible para los usuarios.", "normal", None],
                        ["deception2", "Ya que los softwares de código abierto no libres no cuentan.", "normal", None],
                        ["normal", "Existen muchos videojuegos libres y de código abierto.", "normal", None],
                        ["happy", "Uno que puedes conocer es Friday Night Funkin'.", "excuse", None],
                        ["happy", "Y Virtual Date! también, jeje.", "excuse", None],
                        ["normal", "Yo creo que cuando hacemos videojuegos que son libres y de código abierto, estamos diciéndole a nuestros jugares que nos interesan.", "normal", None],
                        ["normal", "Ya que no solo estamos dándole el código de nuestro juego.", "excuse", None],
                        ["happy", "También le estamos dando algo que pueden usar para aprender de nosotros.", "excuse", None],
                        ["normal", "Y si se encuentra un error ellos rápidamente se encargaran de resolverlo si tienen los conocimientos para hacerlo.", "normal", None],
                        ["normal", "Así aprendemos y nos ayudamos mutuamente.", "excuse", None],
                        ["happy", "Y así nos vamos generando una comunidad que se apoya mutuamente.", "excuse", None],
                        ["normal", "Creo que el software libre y el código abierto es el futuro de los videojuegos.", "normal", None],
                        ["normal", "Ya que a veces creo que los mismos usuarios están más atentos a cualquier error de un videojuego que los mismos desarrolladores.", "normal", None],
                        ["normal", "No sé si tú piensas igual.", "normal", None],
                        ["normal", "", "normal", "exp:4"]
                        ],

                        "2":
                        [
                        ["normal", "Las novelas visuales son un tipo de videojuegos que se basan en su mayor parte en texto.", "normal", None],
                        ["normal", "Su origen es japonés por lo que encontraras muchas novelas visuales que provienen de Japón.", "normal", None],
                        ["normal", "Las novelas visuales es como la versión grafica de las novelas ligeras.", "excuse", None],
                        ["normal", "Su principal forma de contar historias es mediante una caja de texto.", "date", None],
                        ["happy", "Como la que estás viendo ahorita.", "date", None],
                        ["normal", "Los personajes en la historia son representados por sprites.", "normal", None],
                        ["normal", "Ellas contienen una banda sonora, y efectos de sonido para mejorar la experiencia en el juego.", "normal", None],
                        ["normal", "Las historias pueden ser con toma de decisiones que afectan el final, o simplemente tener una historia lineal.", "date", None],
                        ["normal", "Debido a que las novelas visuales son juegos que no requieren mucho presupuesto, los desarrolladores independientes japoneses tienden a centrarse mucho en este tipo de juegos.", "date", None],
                        ["normal", "Ellas pueden estar escritas desde cero o usar herramientas automatizadas como Ren'Py.", "date", None],
                        ["normal", "Usualmente las novelas visuales son representadas con estilo anime sin importar de donde provienen.", "normal", None],
                        ["normal", "Existen varios géneros de novelas visuales.", "date", None],
                        ["normal", "Entre los más conocidos son los simuladores de citas.", "date", None],
                        ["normal", "Que son lo mismo que una novela visual regular.", "normal", None],
                        ["normal", "Solo que esta trata más con temas románticos.", "normal", None],
                        ["normal", "Y tienen objetivos en ellos.", "date", None],
                        ["normal", "Que normalmente son intentar atraer a una o varias chicas.", "normal", None],
                        ["normal", "Existen muchas novelas visuales interesantes.", "normal", None],
                        ["happy", "Así que si quieres entrar en este género de videojuegos, siéntete libre de buscar.", "normal", None],
                        ["normal", "Aunque ya estás jugando un simulador de citas.", "normal", None],
                        ["happy", "Jeje.", "normal", None],
                        ["happy", "", "normal", "exp:4"]
                        ],

                        "3":
                        [
                        ["normal", "Sabes existe una novela visual que sus tiempos fue extremadamente popular.", "normal", None],
                        ["normal", "No sé si la conoces.", "normal", None],
                        ["happy", "Pero estoy hablando de Doki Doki Literature Club!.", "normal", None],
                        ["normal", "Una novela visual que fue lanzada el 22 de septiembre de 2017 por Team Salvato.", "normal", None],
                        ["normal", "Está novela visual fue un existo debido que aunque tiene un aspecto muy agradable.", "excuse", None],
                        ["normal", "Esconde secreto y cosas oscuras.", "excuse", None],
                        ["happy", "Doki Doki Literature Club! es realmente fascinante.", "normal", None],
                        ["normal", "La popularidad de DDLC fue tan grande que se crearon miles de modificaciones del juego.", "normal", None],
                        ["happy", "Actualmente se siguen creando.", "excuse", None],
                        ["jeje", "Pero no son tan populares como haces años.", "excuse", None],
                        ["normal", "Sin duda DDLC cambio la forma de ver las novelas visuales.", "normal", None],
                        ["happy", "Tan popular fue que hasta llego a Japón.", "normal", None],
                        ["normal", "Sabes, DDLC cambio la vida de muchos.", "normal", None],
                        ["normal", "No solo crearon modificaciones del juego.", "normal", None],
                        ["normal", "Si no que cambio su forma de pensar.", "normal", None],
                        ["jeje", "Y creo que hizo a muchos entrar en el mundo del desarrollado de videojuegos.", "normal", None],
                        ["normal", "Actualmente ya no es tan popular, pero todavía hay una comunidad que la mantiene viva.", "normal", None],
                        ["happy", "Quien sabe si algún día vuelve a ser popular.", "normal", None],
                        ["normal", "Si no la conoces, entonces te recomiendo jugarla.", "normal", None],
                        ["happy", "Y si ya la conoces y la haz jugado entonces estarás de acuerdo con lo que dije.", "normal", None],
                        ["happy", "", "normal", "exp:3"]
                        ],

                        "4":
                        [
                        ["normal", "FNAF o Five Nights at Freddy's es un videojuego de terror lanzado en 2014.", "normal", None],
                        ["normal", "Fue desarrollado por Scott Cawthon.", "excuse", None],
                        ["normal", "Debido a una crítica anterior a un videojuego desarrollado por el mismo.", "normal", None],
                        ["normal", "Scott Cawthon tomo esa crítica y la convirtió en lo que conocemos hoy actualmente como FNAF.", "date", None],
                        ["normal", "A pesar de tener años que fue lanzado el primer juego, FNAF sigue siendo un juego muy querido.", "normal", None],
                        ["happy", "De hecho el cambio lo que conocía como terror en esa época.", "normal", None],
                        ["normal", "La jugabilidad del juego en su mayor parte se basa en ver cámaras y cerrar puertas.", "normal", None],
                        ["normal", "En el segundo juego es casi lo mismo solo que se cambia la jugabilidad de cerrar puertas por alumbrar un pasillo y dos conductos.", "normal", None],
                        ["normal", "Y se agrega una máscara con la que te podrás defender.", "excuse", None],
                        ["normal", "En el tercer juego solo puedes ver las cámaras y usar un audio para alejar al único antagonista del juego.", "normal", None],
                        ["jeje", "Los demás juego cambiaron esa jugabilidad por otras, que si ya los conoces entonces debes de saber.", "normal", None],
                        ["normal", "La popularidad de FNAF fue y es tan grande que los fans comenzaron a crear Fangames del juego.", "normal", None],
                        ["embarrassed", "Muchos están bien hechos y otros no.", "normal", None],
                        ["normal", "Actualmente existen varios Fangames muy populares.", "normal", None],
                        ["normal", "Entre son: One Night at Flumpty's y Five Nights at Candy's.", "excuse", None],
                        ["jeje", "Existen más que son muy populares pero esos son los que recuerdo.", "excuse", None],
                        ["normal", "Esos Fangames populares forman parte de lo que se conoce como el Fazbear Fanverse.", "normal", None],
                        ["normal", "Es una iniciativa creada por Scott Cawthon para apoyar a creadores de Fangames de FNAF.", "excuse", None],
                        ["normal", "Actualmente no hay muchos Fangames seleccionados.", "normal", None],
                        ["normal", "Pero Scott Cawthon tiene planes de agregar más en el futuro.", "normal", None],
                        ["normal", "FNAF sin duda es un juego que sigue atrayendo nuevos jugadores.", "normal", None],
                        ["happy", "En muchos años FNAF seguirá siendo muy conocido.", "normal", None],
                        ["happy", "Hasta volverá a ser tan popular como antes.", "excuse", None],
                        ["normal", "Sin duda es un juego increíble.", "normal", None],
                        ["jeje", "Solo que su historia es muy compleja de entender.", "normal", None],
                        ["neutral2", "Lo malo es que el creador del juego se retiró del desarrollo del juego.", "normal", None],
                        ["deception2", "Por una crítica que los fans le hicieron por este haber donado dinero a un politico que muchos no quieren.", "normal", None],
                        ["deception2", "Esos 'fans' hasta lo amenazaron de muerte solo por eso.", "normal", None],
                        ["neutral", "Si no fuera por esas críticas y esas amenazas de muerte, el no se hubiera retirado.", "normal", None],
                        ["neutral2", "Realmente algo que pienso de eso es que los 'fans' no tuvieron por qué importarles eso.", "normal", None],
                        ["neutral", "Siguen y quieren a Scott Cawthon por FNAF no por nada más.", "normal", None],
                        ["neutral2", "Todos tenemos nuestros ideales y a quien apoyar.", "normal", None],
                        ["neutral", "Nadie tenía el derecho de criticarlo por eso.", "normal", None],
                        ["neutral2", "Pero lamentablemente ya no hay vuelta atrás.", "normal", None],
                        ["normal", "Bueno, creo que eso es todo lo que tengo que decir.", "normal", None],
                        ["happy", "Si conoces FNAF, que bien.", "normal", None],
                        ["happy", "Y si no lo conoces te invito a jugarlo.", "excuse", None],
                        ["happy", "Te aseguro que te encantara", "normal", None],
                        ["normal", "Quien sabe y hasta te de la idea de crear tu propio Fangame.", "normal", None],
                        ["happy", "Jeje.", "normal", None],
                        ["normal", "", "normal", "exp:4"]
                        ],

                        "5":
                        [
                        ["normal", "Que bueno que lo preguntas.", "normal", None],
                        ["happy", "Si quieres entrar en el mundo del desarrollado de videojuegos.", "normal", None],
                        ["happy", "Entonces necesitas un motor de videojuegos.", "excuse", None],
                        ["normal", "Un motor de videojuegos es un software que permite crear videojuegos.", "normal", None],
                        ["normal", "Pueden ser gratuitos, libres y de pago.", "normal", None],
                        ["normal", "Existen muchos, y algunos son.", "date", None],
                        ["normal", "Unreal Engine, Unity, Game Maker Studio...", "excuse", None],
                        ["normal", "Godot, Game Salad, Clickteam Fusion...", "excuse", None],
                        ["normal", "Ren'Py, GDevelop, CryEngine...", "excuse", None],
                        ["normal", "Stencyl, Construct y otros más", "excuse", None],
                        ["normal", "Pero no solo existen motores.", "normal", None],
                        ["happy", "Pygame no es un motor de videojuegos pero puedes hacer uno con el.", "date", None],
                        ["normal", "También existen los módulos para desarrollar videojuegos.", "date", None],
                        ["normal", "Tenemos a Love2D, Bevy, HaxeFlixel...", "normal", None],
                        ["happy", "Y muchos más.", "normal", None],
                        ["normal", "De los que nombre muchos son software privativo y otros software libre.", "normal", None],
                        ["normal", "Te recomiendo es usar software libre.", "normal", None],
                        ["normal", "Debido a muchos de los softwares privativos que mencione muchos son de pago.", "normal", None],
                        ["jeje", "Y no son muy baratos.", "normal", None],
                        ["happy", "Pygame es software libre y es realmente bueno.", "normal", None],
                        ["normal", "No creas que con los motores y módulos libres no puedes hacer juegos increíbles.", "normal", None],
                        ["normal", "Te recomiendo ver la conversación 'Herramientas libre y código abierto'.", "date", None],
                        ["normal", "Allí me enfatizare en las herramientas libres para el desarrollo de videojuegos.", "date", None],
                        ["normal", "", "normal", "exp:4"]
                        ],

                        "6":
                        [
                        ["normal", "Bueno, si quieres crear un videojuego.", "normal", None],
                        ["normal", "Existen muchas herramientas o motores para ello.", "date", None],
                        ["normal", "Muchas son privativos y de pago.", "normal", None],
                        ["normal", "Pero intentemos apoyar al software libre.", "normal", None],
                        ["normal", "Existen muchas herramientas libres para la creación de videojuegos.", "date", None],
                        ["normal", "Una de las más populares es Godot.", "normal", None],
                        ["normal", "Godot es un motor de videojuegos que permite desarrollar videojuegos en 2d y 3d.", "normal", None],
                        ["normal", "Se puede programar usando los lenguajes de programación C++, C# y GDScript que es un lenguaje nativo de Godot.", "date", None],
                        ["normal", "El motor nació en Argentina y actualmente es uno de los 5 motores de videojuegos más usados.", "normal", None],
                        ["normal", "A pesar de todo, él no es tan bueno como los motores privativos.", "normal", None],
                        ["happy", "Pero sin duda vale la pena usarlo.", "normal", None],
                        ["normal", "Tenemos también a GDevelop.", "normal", None],
                        ["normal", "GDevelop es un motor de videojuegos pero a diferencia de Godot este solo es para hacer juegos en 2d.", "date", None],
                        ["normal", "En GDevelop no se programa, se usa un sistema de eventos para crear el juego.", "normal", None],
                        ["happy", "Aunque en él no se programa en su mayor parte, puedes extender el motor usando JavaScript para mejorar tu juego.", "excuse", None],
                        ["normal", "También tenemos a Ren'Py.", "normal", None],
                        ["normal", "Un motor de videojuegos para la creación de novelas visuales.", "date", None],
                        ["jeje", "Si, sé que no muchos lo usaría por esa limitación.", "date", None],
                        ["normal", "Con Ren'Py puedes crear un juego fácilmente mediante su lenguaje de scripting.", "date", None],
                        ["happy", "Puedes crear novelas visuales simples o complejas.", "normal", None],
                        ["normal", "Bueno, esos son los motores que conozco.", "normal", None],
                        ["normal", "Pero también están los módulos o bibliotecas.", "date", None],
                        ["normal", "Entre ellas tenemos a Pygame.", "normal", None],
                        ["happy", "la biblioteca para Python que permite desarrollar videojuegos y con el que se hizo este juego.", "date", None],
                        ["normal", "También tenemos a Love2D.", "normal", None],
                        ["normal", "Una biblioteca para desarrollar con el lenguaje de programación Lua.", "normal", None],
                        ["normal", "Está escrito en C++ pero usa Lua para programar los juegos.", "excuse", None],
                        ["jeje", "Realmente no puedo decir mucho de todas las bibliotecas que mencionare ya que solo uso Pygame.", "excuse", None],
                        ["normal", "También tenemos a Bevy.", "normal", None],
                        ["normal", "Que es una biblioteca para desarrollar videojuegos con el lenguaje de programación Rust.", "excuse", None],
                        ["normal", "HaxeFlixel es una biblioteca para el desarrollo de videojuegos con el lenguaje de programación Haxe.", "excuse", None],
                        ["normal", "Está biblioteca se usó para desarrollar al videojuego Friday Night Funkin'.", "normal", None],
                        ["normal", "Esta biblioteca al igual que las otras usan lenguajes de programación que no son muy sencillos de usar.", "excuse", None],
                        ["normal", "Pygame por su parte usa Python.", "normal", None],
                        ["jeje", "Por lo que aprender con Pygame sería más sencillo que aprender con Bevy o HaxeFlixel.", "normal", None],
                        ["normal", "Bueno esas son todas las herramientas que conozco.", "normal", None],
                        ["normal", "Existen muchas pero solo conozco esas.", "excuse", None],
                        ["normal", "En Youtube puedes encontrar tutoriales para desarrollar videojuegos con esas herramientas.", "excuse", None],
                        ["normal", "Solo escoge la más conveniente para ti.", "normal", None],
                        ["happy", "Y entra al maravilloso mundo del desarrollo de videojuegos.", "excuse", None],
                        ["happy", "Jeje.", "normal", None],
                        ["normal", "", "normal", "exp:5"]
                        ]

                        }

videogames_numbers_en = {

                        "0":
                        [
                        ["neutral2", "Good...", "normal", None],
                        ["neutral", "Not really.", "normal", None],
                        ["neutral", "That's a belief that many parents have promoted.", "normal", None],
                        ["neutral2", "Obsession with them is bad.", "normal", None],
                        ["normal", "But they're really not bad.", "normal", None],
                        ["happy", "Actually they have a lot of benefits.", "date", None],
                        ["normal", "Among those benefits are increased concentration.", "normal", None],
                        ["happy", "Playing video games increases concentration and improves decision-making response.", "date", None],
                        ["normal", "They also stimulate the imagination.", "normal", None],
                        ["normal", "And increases basic English learning.", "normal", None],
                        ["normal", "Because many titles are in English.", "normal", None],
                        ["neutral", "Obviously they have their bad things too.", "normal", None],
                        ["neutral", "Like the obsession with them that leads to other problems.", "normal", None],
                        ["neutral2", "Such as neglecting important tasks.", "excuse", None],
                        ["neutral2", "Aggressiveness by not allowing the game.", "normal", None],
                        ["neutral", "And other problems.", "normal", None],
                        ["neutral", "But really they, like excessive use of the computer, do not cause eye damage.", "normal", None],
                        ["neutral2", "Since many parents have promoted the fact that video games damage eyesight.", "excuse", None],
                        ["neutral2", "But it really isn't.", "normal", None],
                        ["neutral2", "A study revealed that video games, like excessive computer use, only cause visual fatigue.", "excuse", None],
                        ["neutral2", "But you won't lose your eyesight for it.", "normal", None],
                        ["neutral", "There are many factors that trigger vision loss.", "normal", None],
                        ["neutral2", "But not that.", "normal", None],
                        ["jeje", "But you still shouldn't spend too much time playing video games or in front of a computer.", "normal", None],
                        ["normal", "But they're really not bad.", "normal", None],
                        ["normal", "", "normal", "exp:4"]
                        ],

                        "1":
                        [
                        ["neutral2", "A question I've been asking myself is whether open source video games will have a future.", "normal", None],
                        ["neutral", "Because companies have no intention of wanting to release the codes of their games.", "normal", None],
                        ["neutral2", "And it crosses my mind that they seem to be hiding something.", "normal", None],
                        ["normal", "But that's not what I mean.", "normal", None],
                        ["normal", "Usually we will find open source games when they are independently developed.", "excuse", None],
                        ["jeje", "So they are not developed by a company.", "excuse", None],
                        ["normal", "And something to say is that I'm talking about free games whose code is available to users.", "normal", None],
                        ["deception2", "Since non-free open source software doesn't count.", "normal", None],
                        ["normal", "There are many free and open source video games out there.", "normal", None],
                        ["happy", "One you might know is Friday Night Funkin'.", "excuse", None],
                        ["happy", "And Virtual Date! too, hehe.", "excuse", None],
                        ["normal", "I think that when we make video games that are free and open source, we are telling our players that we care.", "normal", None],
                        ["normal", "Since we're not just giving you the code for our game.", "excuse", None],
                        ["happy", "We're also giving you something you can use to learn from us.", "excuse", None],
                        ["normal", "And if an error is found they will quickly take care of solving it if they have the knowledge to do it.", "normal", None],
                        ["normal", "This is how we learn and help each other.", "excuse", None],
                        ["happy", "And so we are creating a community that supports each other.", "excuse", None],
                        ["normal", "I think free and open source software is the future of video games.", "normal", None],
                        ["normal", "Since sometimes I think that the same users are more attentive to any error in a video game than the developers themselves.", "normal", None],
                        ["normal", "I don't know if you think the same.", "normal", None],
                        ["normal", "", "normal", "exp:4"]
                        ],

                        "2":
                        [
                        ["normal", "Visual novels are a type of video game that are mostly text-based.", "normal", None],
                        ["normal", "His origin is Japanese so you will find many visual novels that come from Japan.", "normal", None],
                        ["normal", "Visual novels are like the graphic version of light novels.", "excuse", None],
                        ["normal", "Their main way of telling stories is through a text box.", "date", None],
                        ["happy", "Like the one you're looking at right now.", "date", None],
                        ["normal", "The characters in the story are represented by sprites.", "normal", None],
                        ["normal", "They contain a soundtrack, and sound effects to enhance the game experience.", "normal", None],
                        ["normal", "Stories can be with decisions that affect the ending, or just have a linear story.", "date", None],
                        ["normal", "Because visual novels are low-budget games, Japanese indie developers tend to focus a lot on visual novels.", "date", None],
                        ["normal", "They can be written from scratch or use automated tools like Ren'Py.", "date", None],
                        ["normal", "Usually visual novels are rendered in anime style no matter where they come from.", "normal", None],
                        ["normal", "There are various genres of visual novels.", "date", None],
                        ["normal", "Among the best known are dating sims.", "date", None],
                        ["normal", "Which are the same as a regular visual novel.", "normal", None],
                        ["normal", "Just that this one deals more with romantic themes.", "normal", None],
                        ["normal", "And they have targets on them.", "date", None],
                        ["normal", "Which are usually trying to attract one or more girls.", "normal", None],
                        ["normal", "There are many interesting visual novels out there.", "normal", None],
                        ["happy", "So if you want to get into this genre of video games, feel free to search.", "normal", None],
                        ["normal", "Even though you're already playing a dating sim.", "normal", None],
                        ["happy", "Hehe.", "normal", None],
                        ["happy", "", "normal", "exp:4"]
                        ],

                        "3":
                        [
                        ["normal", "Do you know there is a visual novel that back then was extremely popular.", "normal", None],
                        ["normal", "I don't know if you know her.", "normal", None],
                        ["happy", "But I'm talking about Doki Doki Literature Club!.", "normal", None],
                        ["normal", "A visual novel that was released on September 22, 2017 by Team Salvato.", "normal", None],
                        ["normal", "This visual novel was a success because although it looks very nice.", "excuse", None],
                        ["normal", "Hide secret and dark things.", "excuse", None],
                        ["happy", "Doki Doki Literature Club! is really fascinating.", "normal", None],
                        ["normal", "The popularity of DDLC was so great that thousands of mods of the game were created.", "normal", None],
                        ["happy", "Currently still being created.", "excuse", None],
                        ["jeje", "But they are not as popular as years ago.", "excuse", None],
                        ["normal", "DDLC definitely changed the way you see visual novels.", "normal", None],
                        ["happy", "It was so popular that it even came to Japan.", "normal", None],
                        ["normal", "You know, DDLC changed the lives of many.", "normal", None],
                        ["normal", "They didn't just create game mods.", "normal", None],
                        ["normal", "Otherwise it changed your way of thinking.", "normal", None],
                        ["jeje", "And I think it made many people enter the world of game development.", "normal", None],
                        ["normal", "Currently not that popular anymore, but there is still a community that keeps it alive.", "normal", None],
                        ["happy", "Who knows if it will ever be popular again.", "normal", None],
                        ["normal", "If you don't know it, then I recommend you play it.", "normal", None],
                        ["happy", "And if you already know it and have played it then you will agree with what I said.", "normal", None],
                        ["happy", "", "normal", "exp:3"]
                        ],

                        "4":
                        [
                        ["normal", "FNAF or Five Nights at Freddy's is a horror video game released in 2014.", "normal", None],
                        ["normal", "It was developed by Scott Cawthon.", "excuse", None],
                        ["normal", "Due to a previous criticism of a video game developed by himself.", "normal", None],
                        ["normal", "Scott Cawthon took that critique and turned it into what we now know today as FNAF.", "date", None],
                        ["normal", "Despite being years since the first game was released, FNAF is still a much-loved game.", "normal", None],
                        ["happy", "Actually it changed what I knew as horror at that time.", "normal", None],
                        ["normal", "The gameplay of the game for the most part is based on viewing cameras and closing doors.", "normal", None],
                        ["normal", "In the second game it's almost the same except that the gameplay is changed from closing doors to lighting up a corridor and two ducts.", "normal", None],
                        ["normal", "And a mask is added with which you can defend yourself.", "excuse", None],
                        ["normal", "In the third game you can only see the cameras and use an audio to drive away the only antagonist in the game.", "normal", None],
                        ["jeje", "The other games changed that gameplay for others, if you already know them then you should know.", "normal", None],
                        ["normal", "The popularity of FNAF was and is so big that fans started creating Fangames of the game.", "normal", None],
                        ["embarrased", "Many are well done and some are not.", "normal", None],
                        ["normal", "Currently there are several very popular Fangames.", "normal", None],
                        ["normal", "Between are: One Night at Flumpty's and Five Nights at Candy's.", "excuse", None],
                        ["jeje", "There are more that are very popular but those are the ones I remember.", "excuse", None],
                        ["normal", "Those popular Fangames are part of what is known as the Fazbear Fanverse.", "normal", None],
                        ["normal", "It is an initiative created by Scott Cawthon to support creators of FNAF Fangames.", "excuse", None],
                        ["normal", "There are currently not many Fangames selected.", "normal", None],
                        ["normal", "But Scott Cawthon has plans to add more in the future.", "normal", None],
                        ["normal", "FNAF is certainly a game that continues to attract new players.", "normal", None],
                        ["happy", "In many years FNAF will still be very popular.", "normal", None],
                        ["happy", "It'll even be as popular as before again.", "excuse", None],
                        ["normal", "This is definitely an amazing game.", "normal", None],
                        ["jeje", "Just that his story is very complex to understand.", "normal", None],
                        ["neutral2", "The bad thing is that the game creator withdrew from the development of the game.", "normal", None],
                        ["deception2", "Because of a criticism that fans made him for having donated money to a politician that many do not like.", "normal", None],
                        ["deception2", "Those 'fans' even threatened to kill him just because of that.", "normal", None],
                        ["neutral", "If it weren't for those criticisms and death threats, he wouldn't have retired.", "normal", None],
                        ["neutral2", "Actually one thing I think about that is that the 'fans' didn't have to care about that.", "normal", None],
                        ["neutral", "They follow and want Scott Cawthon for FNAF not for anything else.", "normal", None],
                        ["neutral2", "We all have our ideals and someone to support.", "normal", None],
                        ["neutral", "No one had the right to criticize him for that.", "normal", None],
                        ["neutral2", "But unfortunately there is no way back now.", "normal", None],
                        ["normal", "Well, I guess that's all I have to say.", "normal", None],
                        ["happy", "If you know FNAF, great.", "normal", None],
                        ["happy", "And if you don't know it, I invite you to play it.", "excuse", None],
                        ["happy", "I'm sure you'll love it", "normal", None],
                        ["normal", "Who knows and even gives you the idea of creating your own Fangame.", "normal", None],
                        ["happy", "Hehe.", "normal", None],
                        ["normal", "", "normal", "exp:4"]
                        ],

                        "5":
                        [
                        ["normal", "It's good that you asked.", "normal", None],
                        ["happy", "If you want to enter the world of game development.", "normal", None],
                        ["happy", "So you need a game engine.", "excuse", None],
                        ["normal", "A game engine is software that allows you to create video games.", "normal", None],
                        ["normal", "They can be free, free and paid.", "normal", None],
                        ["normal", "There are many, and some are.", "date", None],
                        ["normal", "Unreal Engine, Unity, Game Maker Studio...", "excuse", None],
                        ["normal", "Godot, Game Salad, Clickteam Fusion...", "excuse", None],
                        ["normal", "Ren'Py, GDevelop, CryEngine...", "excuse", None],
                        ["normal", "Stencyl, Construct and others", "excuse", None],
                        ["normal", "But there are not only engines.", "normal", None],
                        ["happy", "Pygame is not a game engine but you can make one with it.", "date", None],
                        ["normal", "There are also modules for developing video games.", "date", None],
                        ["normal", "We have Love2D, Bevy, HaxeFlixel...", "normal", None],
                        ["happy", "And many more.", "normal", None],
                        ["normal", "Many of which you name are proprietary software and other free software.", "normal", None],
                        ["normal", "I recommend you use free software.", "normal", None],
                        ["normal", "Due to many of the proprietary software I mentioned many are paid.", "normal", None],
                        ["jeje", "And they're not very cheap.", "normal", None],
                        ["happy", "Pygame is free software and it's really good.", "normal", None],
                        ["normal", "Don't think that with free engines and modules you can't make amazing games.", "normal", None],
                        ["normal", "I recommend you to see the conversation 'Free and open source tools'.", "date", None],
                        ["normal", "There I will emphasize free tools for video game development.", "date", None],
                        ["normal", "", "normal", "exp:4"]
                        ],

                        "6":
                        [
                        ["normal", "Well, if you want to make a game.", "normal", None],
                        ["normal", "There are many tools or engines for this.", "date", None],
                        ["normal", "Many are proprietary and paid.", "normal", None],
                        ["normal", "But let's try to support free software.", "normal", None],
                        ["normal", "There are many free tools for creating video games.", "date", None],
                        ["normal", "One of the most popular is Godot.", "normal", None],
                        ["normal", "Godot is a game engine that allows you to develop 2d and 3d video games.", "normal", None],
                        ["normal", "It can be programmed using the programming languages C++, C# and GDScript which is a native Godot language.", "date", None],
                        ["normal", "The engine was born in Argentina and is currently one of the 5 most used game engines.", "normal", None],
                        ["normal", "Regardless, it's not as good as proprietary engines.", "normal", None],
                        ["happy", "But it's definitely worth using.", "normal", None],
                        ["normal", "We also have GDevelop.", "normal", None],
                        ["normal", "GDevelop is a game engine but unlike Godot it is only for making 2d games.", "date", None],
                        ["normal", "GDevelop does not program, an event system is used to create the game.", "normal", None],
                        ["happy", "Although most of it doesn't program, you can extend the engine using JavaScript to improve your game.", "excuse", None],
                        ["normal", "We also have Ren'Py.", "normal", None],
                        ["normal", "A game engine for creating visual novels.", "date", None],
                        ["jeje", "Yes, I know not many would use it because of that limitation.", "date", None],
                        ["normal", "With Ren'Py you can easily create a game using its scripting language.", "date", None],
                        ["happy", "You can create simple or complex visual novels.", "normal", None],
                        ["normal", "Well, those are the engines I know.", "normal", None],
                        ["normal", "But there are also modules or libraries.", "date", None],
                        ["normal", "Among them we have Pygame.", "normal", None],
                        ["happy", "the library for Python that supports video game development and with which this game was made.", "date", None],
                        ["normal", "We also have Love2D.", "normal", None],
                        ["normal", "A library for developing with the Lua programming language.", "normal", None],
                        ["normal", "It is written in C++ but uses Lua to program the games.", "excuse", None],
                        ["jeje", "I really can't say much about all the libraries I'm going to mention since I only use Pygame.", "excuse", None],
                        ["normal", "We also have Bevy.", "normal", None],
                        ["normal", "What is a library to develop video games with the Rust programming language.", "excuse", None],
                        ["normal", "HaxeFlixel is a library for the development of video games with the Haxe programming language.", "excuse", None],
                        ["normal", "This library was used to develop Friday Night Funkin'.", "normal", None],
                        ["normal", "This library, like the others, uses programming languages that are not very easy to use.", "excuse", None],
                        ["normal", "Pygame for its part uses Python.", "normal", None],
                        ["jeje", "So learning with Pygame would be easier than learning with Bevy or HaxeFlixel.", "normal", None],
                        ["normal", "Well those are all the tools I know of.", "normal", None],
                        ["normal", "There are many but I only know those.", "excuse", None],
                        ["normal", "On Youtube you can find tutorials to develop video games with these tools.", "excuse", None],
                        ["normal", "Just choose the most convenient for you.", "normal", None],
                        ["happy", "And enter the wonderful world of game development.", "excuse", None],
                        ["happy", "Hehe.", "normal", None],
                        ["normal", "", "normal", "exp:5"]
                        ]

                        }

### Virtual Date!

virtual_date_subthemes_es =  {

                                "themes":
                                        [
                                        "¿Prototipo?",
                                        "Características faltantes.",
                                        "Errores comunes.",
                                        "Se corta los diálogos en la caja de texto.",
                                        "¿A 22 FPS?",
                                        "¿Por qué la pantalla del juego es de 1000 x 520?",
                                        "El código fuente."
                                        ],

                                "numbers":
                                        [
                                        "0",
                                        "1",
                                        "2",
                                        "3",
                                        "4",
                                        "5",
                                        "6"
                                        ]
                            }

virtual_date_subthemes_en =  {

                                "themes":
                                        [
                                        "Prototype?",
                                        "Missing features.",
                                        "Common mistakes.",
                                        "Dialogs in the text box are cut.",
                                        "At 22 FPS?",
                                        "Why is the game screen 1000 x 520?",
                                        "The source code."
                                        ],

                                "numbers":
                                        [
                                        "0",
                                        "1",
                                        "2",
                                        "3",
                                        "4",
                                        "5",
                                        "6"
                                        ]
                            }

virtual_date_numbers_es = {

                        "0":
                        [
                        ["normal", "Esa pregunta se responde por si sola.", "normal", None],
                        ["normal", "Como veras, 'Virtual Date!' carece de muchas cosas críticas.", "normal", None],
                        ["normal", "Una de ellas es que no se puede redimensionar la ventana.", "excuse", None],
                        ["jeje", "Algo que es realmente crítico para un juego.", "normal", None],
                        ["normal", "Muchas cosas se eliminaron para este prototipo.", "normal", None],
                        ["jeje", "Que la verdad no es muy bueno.", "normal", None],
                        ["normal", "Pero nos sentimos muy orgullosos por el hecho de que funcione.", "normal", None],
                        ["happy", "Quien diría que Pygame puede hacer esto.", "normal", None],
                        ["normal", "Espera...", "normal", None],
                        ["happy", "Si puede.", "date", None],
                        ["normal", "Esperamos que en futuras actualizaciones el juego sea mejor.", "normal", None],
                        ["normal", "", "normal", "exp:2"]
                        ],

                        "1":
                        [
                        ["normal", "Bueno, las características faltantes de este prototipo son las siguientes.", "normal", None],
                        ["normal", "Se tuvieron que eliminar temas de conversación.", "date", None],
                        ["normal", "Si notas en la pantalla de selección de conversación, no hay una barra de desplazamiento.", "normal", None],
                        ["jeje", "Eso limita el agregar más temas de conversación y por ende se limitan en base al tamaño de la pantalla.", "normal", None],
                        ["normal", "Algunas características eliminadas dependen del redimensionado de la pantalla del juego.", "normal", None],
                        ["jeje", "Y otras creo que no sería bueno decirlas para no spoilear.", "normal", None],
                        ["normal", "Pero si se eliminaron muchas.", "normal", None],
                        ["normal", "", "normal", "exp:2"]
                        ],

                        "2":
                        [
                        ["normal", "Algunas errores que puedes encontrar en el juego son:...", "normal", None],
                        ["normal", "'El juego no se ejecuta'.", "excuse", None],
                        ["normal", "Uno de los motivos por que el juego no se ejecute es no tener suficiente memoria RAM libre para el juego.", "normal", None],
                        ["normal", "El juego requiere al menos 600 MB de memoria RAM libre para su ejecución.", "normal", None],
                        ["normal", "Otro error es el que Python no encuentre una animación es mis sprites.", "date", None],
                        ["jeje", "Si ves el código fuente del juego y ves la cantidad de temas de conversación, veras que equivocarse no es algo difícil.", "normal", None],
                        ["normal", "Otro error es que la data puede ser que no se guarde.", "normal", None],
                        ["normal", "Si estás ejecutando el juego en una ubicación de solo lectura o el mismo sistema operativo no le permite escribir archivos, el juego no guardara la data.", "normal", None],
                        ["jeje", "Un error común es el alto consumo de recursos siendo un juego tan pequeño.", "normal", None],
                        ["normal", "Esos creo que son los errores que te encontraras normalmente.", "normal", None],
                        ["normal", "Cualquier error puedes notificarlo en Github en donde está alojado el código fuente.", "excuse", None],
                        ["normal", "", "normal", "exp:2"]
                        ],

                        "3":
                        [
                        ["normal", "Bueno, algo has notado en la caja de texto...", "normal", None],
                        ["normal", "Y es que los diálogos se cortan.", "normal", None],
                        ["jeje", "Ósea que las letras se cortan y pasan a otra línea.", "normal", None],
                        ["jeje", "Ese es uno de los problemas que queremos eliminar.", "normal", None],
                        ["jeje", "Y no sabemos cómo.", "normal", None],
                        ["normal", "Pero creo que lo bueno es que funciona.", "normal", None],
                        ["jeje", "¿No?", "excuse", None],
                        ["normal", "", "normal", "exp:2"]
                        ],

                        "4":
                        [
                        ["normal", "Bueno, algo que puedes no llegar a creer.", "normal", None],
                        ["normal", "Es que el juego se hizo a 22 FPS.", "normal", None],
                        ["normal", "Esto debido a que la computadora de desarrollo no es muy buena que digamos.", "normal", None],
                        ["normal", "Y a medida que iba aumentando el peso de mi sprite y el fondo, el juego se redujo a solo correr a 1, 2 o 3 FPS.", "normal", None],
                        ["normal", "Con el antialiasing desactivado corre entre los 8 FPS, pero al abrir el menú de conversación corre a solo 2 FPS.", "excuses", None],
                        ["normal", "Mientras otros con PC súper potentes no hacen nada con ellas.", "normal", None],
                        ["happy", "Nosotros con PC de gama muy baja intentamos hacer videojuegos.", "excuse", None],
                        ["normal", "Así que lo que quiero decir es que no se necesita un PC súper poderoso para hacer un videojuego.", "normal", None],
                        ["happy", "Solo tienes que aprovechar lo que tienes.", "date", None],
                        ["normal", "", "normal", "exp:2"]
                        ],

                        "5":
                        [
                        ["normal", "Esto porque el juego no cuenta con la redimensión de pantalla y de los gráficos.", "normal", None],
                        ["embarrassed", "Eso es un poco complicado de hacer.", "normal", None],
                        ["embarrassed", "Y hablo de la redimensión de los gráficos.", "normal", None],
                        ["sad3", "Ya que eso usa algunos cálculos matemáticos que no poseemos.", "normal", None],
                        ["embarrassed", "Así que puedes burlarte si quieres.", "normal", None],
                        ["normal", "Pero en futuras versiones esperamos que ya el juego no sea así.", "normal", None],
                        ["normal", "", "normal", "exp:2"]
                        ],

                        "6":
                        [
                        ["normal", "Como debes de saber el juego es libre y de código abierto.", "normal", None],
                        ["normal", "Y eso quiere decir que puedes obtener el código fuente sin ningún problema.", "date", None],
                        ["normal", "Está disponible en Github, y puedes descargarlo si lo deseas.", "normal", None],
                        ["normal", "Si ves un error en el juego y tienes los conocimientos para hacerlo eres bienvenido o bienvenida a hacerlo.", "normal", None],
                        ["happy", "Estaremos muy felices por recibir ayuda.", "normal", None],
                        ["normal", "", "normal", "exp:2"]
                        ]

                        }

virtual_date_numbers_en = {

                        "0":
                        [
                        ["normal", "That question answers itself.", "normal", None],
                        ["normal", "As you see, 'Virtual Date!' lacks many critical things.", "normal", None],
                        ["normal", "One of them is that you can't resize the window.", "excuse", None],
                        ["jeje", "Something that is really critical for a game.", "normal", None],
                        ["normal", "Many things were removed for this prototype.", "normal", None],
                        ["jeje", "That's really not very good.", "normal", None],
                        ["normal", "But we are very proud that it works.", "normal", None],
                        ["happy", "Who knew that Pygame can do this.", "normal", None],
                        ["normal", "Wait...", "normal", None],
                        ["happy", "If you can.", "date", None],
                        ["normal", "Hopefully in future updates the game will be better.", "normal", None],
                        ["normal", "", "normal", "exp:2"]
                        ],

                        "1":
                        [
                        ["normal", "Well, the missing features of this prototype are as follows.", "normal", None],
                        ["normal", "Had to delete threads.", "date", None],
                        ["normal", "If you notice on the conversation selection screen, there is no scroll bar.", "normal", None],
                        ["jeje", "That limits adding more threads and therefore they are limited based on the size of the screen.", "normal", None],
                        ["normal", "Some features removed depend on game screen resizing.", "normal", None],
                        ["jeje", "And others I think it would not be good to say them so as not to spoil.", "normal", None],
                        ["normal", "But many were removed.", "normal", None],
                        ["normal", "", "normal", "exp:2"]
                        ],

                        "2":
                        [
                        ["normal", "Some errors you may encounter in the game are:...", "normal", None],
                        ["normal", "'Game doesn't start'.", "excuse", None],
                        ["normal", "One of the reasons the game won't run is because I don't have enough free RAM for the game.", "normal", None],
                        ["normal", "The game requires at least 600 MB of free RAM to run.", "normal", None],
                        ["normal", "Another error is that Python can't find an animation in my sprites.", "date", None],
                        ["jeje", "If you look at the source code of the game and see the number of topics of conversation, you will see that being wrong is not difficult.", "normal", None],
                        ["normal", "Another error is that the data may not be saved.", "normal", None],
                        ["normal", "If you are running the game in a read-only location or the operating system itself does not allow it to write files, the game will not save data.", "normal", None],
                        ["jeje", "A common error is the high consumption of resources for such a small game.", "normal", None],
                        ["normal", "I think those are the errors you will normally encounter.", "normal", None],
                        ["normal", "Any bug you can report on Github where the source code is hosted.", "excuse", None],
                        ["normal", "", "normal", "exp:2"]
                        ],

                        "3":
                        [
                        ["normal", "Well, did you notice something in the text box...", "normal", None],
                        ["normal", "And it is that the dialogs are cut.", "normal", None],
                        ["jeje", "That is, the letters are cut off and moved to another line.", "normal", None],
                        ["jeje", "That's one of the problems we want to eliminate.", "normal", None],
                        ["jeje", "And we don't know how.", "normal", None],
                        ["normal", "But I think the good thing is that it works.", "normal", None],
                        ["jeje", "No?", "excuse", None],
                        ["normal", "", "normal", "exp:2"]
                        ],

                        "4":
                        [
                        ["normal", "Well, something you might not believe.", "normal", None],
                        ["normal", "The game was made at 22 FPS.", "normal", None],
                        ["normal", "This is because the development computer is not very good to say.", "normal", None],
                        ["normal", "And as the weight of my sprite and background increased, the game slowed down to just running at 1, 2 or 3 FPS.", "normal", None],
                        ["normal", "With antialiasing disabled it runs between 8 FPS, but when you open the chat menu it runs at only 2 FPS.", "excuses", None],
                        ["normal", "While others with super powerful PCs do nothing with them.", "normal", None],
                        ["happy", "We with very low-end PCs try to make video games.", "excuse", None],
                        ["normal", "So what I mean is that you don't need a super powerful PC to make a video game.", "normal", None],
                        ["happy", "You just have to take advantage of what you have.", "date", None],
                        ["normal", "", "normal", "exp:2"]
                        ],

                        "5":
                        [
                        ["normal", "This is because the game does not have the screen and graphics resizing.", "normal", None],
                        ["embarrassed", "That's a bit tricky to do.", "normal", None],
                        ["embarrased", "And I'm talking about resizing the graphics.", "normal", None],
                        ["sad3", "Since that uses some math we don't have.", "normal", None],
                        ["embarrased", "So you can mock if you want.", "normal", None],
                        ["normal", "But in future versions we hope that the game will no longer be like this.", "normal", None],
                        ["normal", "", "normal", "exp:2"]
                        ],

                        "6":
                        [
                        ["normal", "As you should know the game is free and open source.", "normal", None],
                        ["normal", "And that means you can get the source code without any problem.", "date", None],
                        ["normal", "It's available on Github, and you can download it if you want.", "normal", None],
                        ["normal", "If you see an error in the game and you have the knowledge to do it, you are welcome to do it.", "normal", None],
                        ["happy", "We will be very happy to receive help.", "normal", None],
                        ["normal", "", "normal", "exp:2"]
                        ]

                        }

# life_subthemes_es = {

#                     "themes":
#                             [
#                             ],

#                     "numbers":
#                             [
#                             ]
#                     }

# life_subthemes_en = {}

welcome_to_virtual_date_es = [
                             ["happy", "Hola!!!", "hi", None],
                             ["happy", "Mi nombre es Tojiko Merata.", "hi", None],
                             ["happy", "Bienvenido o bienvenida a Virtual Date!", "hi", None],
                             ["happy", "Será un placer pasar el tiempo contigo.", "normal", None],
                             ["normal", "Bueno, ya que estás aquí te diré que este juego es súper sencillo de jugar.", "date", None],
                             ["happy", "Por lo que déjame darte un pequeño 'Tutorial'.", "date", None],
                             ["normal", "El juego está hecho para tener una 'cita' conmigo.", "date", None],
                             ["jeje", "Por eso el nombre.", "date", None],
                             ["normal", "Podemos hacer varias cosas aquí…", "normal", None],
                             ["happy", "Podemos charlar, escuchar música y...", "date", None],
                             ["jeje", "Lo siento pero eso es lo que podemos hacer por ahora, jeje.", "date", None],
                             ["normal", "El botón 'Hablar' es el que te permitirá charlar conmigo.", "normal", None],
                             ["normal", "El conversar te ayuda a ganar puntos de experiencia que te servirán para desbloquear nuevas conversaciones.", "date", None],
                             ["happy", "Y así conversar de más temas interesantes.", "normal", None],
                             ["normal", "El botón música te permitirá escuchar una música por defecto en el juego.", "date", None],
                             ["jeje", "Si, en próximas versiones se incluirá el poder escuchar música personalizada.", "date", None],
                             ["normal", "El botón 'Cámara' te permitirá cambiar el zoom del juego, por lo que si sientes que estoy demasiado cerca o lejos, podrás cambiarlo.", "date", None],
                             ["jeje", "Eso es todo lo que te puedo decir.", "normal", None],
                             ["jeje", "En el tema de conversación 'Virtual Date!' se explica más cosas sobre el juego, que te pueden interesar.", "normal", None],
                             ["normal", "Como los errores comunes, las características que se eliminaron de este prototipo y más.", "normal", None],
                             ["happy", "Siéntete libre de echarle un ojo.", "normal", None],
                             ["normal", "Y ahora...", "normal", None],
                             ["happy", "¿Qué haremos?", "normal", None],
                             ["normal", "...", "normal", "no_talk"],
                             ["normal", "Casi se me olvida, cuando vayas a cerrar el juego ve y di 'Adiós' para poder guardar los datos.", "date", None],
                             ["jeje", "Así que no cierres el juego de golpe, puedes perder lo que hiciste.", "date", None],
                             ["jeje", "También se siente extraño cuando el juego se cierra de la nada.", "date", None],
                             ["happy", "Así que por favor di 'Adiós'.", "normal", None],
                             ["normal", "Eso es todo lo que tengo que decir.", "normal", None],
                             ["happy", "", "normal", None]
                             ]

welcome_to_virtual_date_en = [
                            ["happy", "Hello!!!", "hi", None],
                            ["happy", "My name is Tojiko Merata.", "hi", None],
                            ["happy", "Welcome to Virtual Date!", "hi", None],
                            ["happy", "It will be a pleasure to spend time with you.", "normal", None],
                            ["normal", "Well, while you're here I'll tell you that this game is super easy to play.", "date", None],
                            ["happy", "So let me give you a little 'Tutorial'.", "date", None],
                            ["normal", "The game is made to 'date' me.", "date", None],
                            ["jeje", "Hence the name.", "date", None],
                            ["normal", "We can do several things here...", "normal", None],
                            ["happy", "We can chat, listen to music and...", "date", None],
                            ["jeje", "Sorry but that's what we can do for now, hehe.", "date", None],
                            ["normal", "The 'Talk' button is the one that will allow you to chat with me.", "normal", None],
                            ["normal", "Talking helps you gain experience points that will help you unlock new conversations.", "date", None],
                            ["happy", "And so talk about more interesting topics.", "normal", None],
                            ["normal", "The music button will allow you to listen to the default music in the game.", "date", None],
                            ["jeje", "Yes, in future versions the ability to listen to personalized music will be included.", "date", None],
                            ["normal", "The 'Camera' button will allow you to change the zoom of the game, so if you feel I'm too close or too far, you can change it.", "date", None],
                            ["jeje", "That's all I can tell you.", "normal", None],
                            ["jeje", "In the topic of conversation 'Virtual Date!' more things about the game are explained, that may interest you.", "normal", None],
                            ["normal", "Such as common bugs, features that were removed from this prototype, and more.", "normal", None],
                            ["happy", "Feel free to check it out.", "normal", None],
                            ["normal", "And now...", "normal", None],
                            ["happy", "what shall we do?", "normal", None],
                            ["normal", "...", "normal", "no_talk"],
                            ["normal", "I almost forgot, when you go to close the game go and say 'Goodbye' so I can save the data.", "date", None],
                            ["jeje", "So don't slam the game, you may lose what you did.", "date", None],
                            ["jeje", "It also feels weird when the game crashes out of nowhere.", "date", None],
                            ["happy", "So please say 'Goodbye'.", "normal", None],
                            ["normal", "That's all I have to say.", "normal", None],
                            ["happy", "", "normal", None]
                            ]

welcome_again_es = [
                   ["happy", "¡Hola de nuevo!", "hi", None],
                   ["happy", "¿Qué quieres hacer hoy?", "excuse", None],
                   ["happy", "", "excuse", "firstrun"]
                   ]

welcome_again_en = [
                   ["happy", "Hello again!", "hi", None],
                   ["happy", "What do you want to do today?", "excuse", None],
                   ["happy", "", "excuse", "firstrun"]
                   ]

# Función para el cambio del lenguaje

def change_languages(language="es"):

    """
    Cambia el lenguaje

    :language: "es" o "en", eso son los lenguajes disponibles

    """

    global types, types_labels, make_compliments, compliments_labels, make_questions, question_labels, i_feel, feel_labels, con_themes
    global art_subthemes, anime_subthemes, history_subthemes, music_subthemes, us_subthemes, python_pygame_subthemes, tojiko_subthemes, videogames_subthemes, virtual_date_subthemes
    global welcome_to_virtual_date, welcome_again

    global art_numbers, anime_numbers, history_numbers, music_numbers, us_numbers, python_pygame_numbers, tojiko_numbers, videogames_numbers, virtual_date_numbers

    if language == "es":

        ##### Secciones prinicipales #####

        types = types_es
        types_labels = types_labels_es
        make_compliments = make_compliments_es
        compliments_labels = compliments_labels_es
        make_questions = make_questions_es
        question_labels = question_labels_es
        i_feel = i_feel_es
        feel_labels = feel_labels_es

        ##### Temás de conversación #####

        con_themes = con_themes_es

        ### Subtemás ###

        art_subthemes = art_subthemes_es
        art_numbers = art_numbers_es

        anime_subthemes = anime_subthemes_es
        anime_numbers = anime_numbers_es

        history_subthemes = history_subthemes_es
        history_numbers = history_numbers_es

        music_subthemes = music_subthemes_es
        music_numbers = music_numbers_es

        us_subthemes = us_subthemes_es
        us_numbers = us_numbers_es

        python_pygame_subthemes = python_pygame_subthemes_es
        python_pygame_numbers = python_pygame_numbers_es

        tojiko_subthemes = tojiko_subthemes_es
        tojiko_numbers = tojiko_numbers_es

        videogames_subthemes = videogames_subthemes_es
        videogames_numbers = videogames_numbers_es

        virtual_date_subthemes = virtual_date_subthemes_es
        virtual_date_numbers = virtual_date_numbers_es

        # Bienvenida

        welcome_to_virtual_date = welcome_to_virtual_date_es
        welcome_again = welcome_again_es

    elif language == "en":

        ##### Secciones prinicipales #####
        
        types = types_en
        types_labels = types_labels_en
        make_compliments = make_compliments_en
        compliments_labels = compliments_labels_en
        make_questions = make_questions_en
        question_labels = question_labels_en
        i_feel = i_feel_en
        feel_labels = feel_labels_en

        ##### Temás de conversación #####

        con_themes = con_themes_en

        ### Subtemás ###

        art_subthemes = art_subthemes_en
        art_numbers = art_numbers_en

        anime_subthemes = anime_subthemes_en
        anime_numbers = anime_numbers_en

        history_subthemes = history_subthemes_en
        history_numbers = history_numbers_en

        music_subthemes = music_subthemes_en
        music_numbers = music_numbers_en

        us_subthemes = us_subthemes_en
        us_numbers = us_numbers_en

        python_pygame_subthemes = python_pygame_subthemes_en
        python_pygame_numbers = python_pygame_numbers_en

        tojiko_subthemes = tojiko_subthemes_en
        tojiko_numbers = tojiko_numbers_en

        videogames_subthemes = videogames_subthemes_en
        videogames_numbers = videogames_numbers_en

        virtual_date_subthemes = virtual_date_subthemes_en
        virtual_date_numbers = virtual_date_numbers_en

        # Bienvenida

        welcome_to_virtual_date = welcome_to_virtual_date_en
        welcome_again = welcome_again_en

# Configuración de language

if config.current_language == "es":

    change_languages("es")

elif config.current_language == "en":

    change_languages("en")