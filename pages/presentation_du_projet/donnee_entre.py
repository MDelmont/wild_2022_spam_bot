#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dash import html,dcc
import plotly.express as px


from modules.conf import Conf

class Donnee_entre():
    def __init__(self, app):
        self.app = app
        self.conf = Conf()

    def get_layout(self):
        layout =html.Div([
        
        
        
                    html.Div([
                                html.H1("Les données d'entrées"),
                            ], style={'textAlign':'center'}),

                    html.Div([
                                html.Div([
                                    html.H2("Les cibles de predictions"),
                                    
                                ], style={'textAlign':'left'}),
                                html.Div([
                                    html.H3("Spam",style={'color':self.conf.red}),
                                    html.P("Spam correspond à un message envoyer généralement par une machine, qui est considéré comme indésirable",className='text-danger')
                                ], style={'width' : '40%','textAlign':'center','display':'inline-block','verticalAlign' : 'top','padding-right' : '5%'}),

                                html.Div([
                                    html.H3("Ham",style={'color':self.conf.bleu}),
                                    html.P("Ham correspond à un message qui est interessant et utile pour l'utilisateur",className='text-primary')
                                ], style={'width' : '40%','textAlign':'center','display':'inline-block','verticalAlign' : 'top','padding-left' : '5%'}),
                            ], style={'textAlign':'center','width' : '80%','padding-left' : '10%'}),





                    html.Div([
                        html.Div([
                            html.H2("Les sms"),
                            
                        ], style={'textAlign':'left'}),
                        html.Div( self.make_layout_spam_ham()
                            
                            
                        , style = {'width' : '100%', 'display': 'inline-block', "overflow": "scroll",'height': '20rem'}),
                    ], style={'textAlign':'center','width' : '100%','padding-left' : '10%',}),

                    html.Div([
                        html.Div([
                            html.H2("Répartition des spam et des ham"),
                            
                        ], style={'textAlign':'left'}),
                        html.Div( self.make_layout_spam_ham()
                            
                            
                        , style = {'width' : '100%', 'display': 'inline-block', "overflow": "scroll",'height': '20rem'}),
                    ], style={'textAlign':'center','width' : '100%','padding-left' : '10%',}),

        

                ])
        return layout



    def make_layout_spam_ham(self):

        list_ham = ["Sorry, I'll call later",
                    "Can you pls send me that company name. In saibaba colany",
                    "U still havent got urself a jacket ah?",
                    "Hey chief, can you give me a bell when you get this. Need to talk to you about this royal visit on the 1st june. ",
                    "Compliments to you. Was away from the system. How your side"]

        list_spam = ["PRIVATE! Your 2003 Account Statement for 07808247860 shows 800 un-redeemed S. I. M. points. Call 08719899229 Identifier Code: 40411 Expires 06/11/04",
                    "ASKED 3MOBILE IF 0870 CHATLINES INCLU IN FREE MINS. INDIA CUST SERVs SED YES. L8ER GOT MEGA BILL. 3 DONT GIV A SHIT. BAILIFF DUE IN DAYS. I O £250 3 WANT £800",
                    "For the most sparkling shopping breaks from 45 per person; call 0121 2025050 or visit www.shortbreaks.org.uk.",
                    "You have won a guaranteed 32000 award or maybe even £1000 cash to claim ur award call free on 0800 ..... (18+). Its a legitimat efreefone number wat do u think???",
                    "You have 1 new message. Call 0207-083-6089 ",
                    "The current leading bid is 151. To pause this auction send OUT. Customer Care: 08718726270"]
        layout_list_ham_spam = []
        for ham in list_ham:
            layout_list_ham_spam.append(self.make_layout_simple('ham',ham))
        for spam in list_spam:
            layout_list_ham_spam.append(self.make_layout_simple('spam',spam))

        return layout_list_ham_spam


    def make_layout_simple(self,categ,text):
        if categ == 'spam':
            return html.Div(children=[
                        html.Div([categ],className='card-header'),

                        html.Div([
                            
                            html.P(text,className='card-text')
                        ],className='card-body'),          
                    ],className='card text-white bg-danger mb-3',style={'width': '20rem','height': '15rem','display': 'inline-block','verticalAlign':'top','padding-left' : '2%','padding-right' : '2%'})
        else:
            return html.Div(children=[
                        html.Div([categ],className='card-header'),

                        html.Div([
                            
                            html.P(text,className='card-text')
                        ],className='card-body'),          
                    ],className='card text-white bg-primary mb-3',style={'width': '20rem','height': '15rem','display': 'inline-block','verticalAlign':'top','padding-left' : '2px','padding-right' : '2px'})