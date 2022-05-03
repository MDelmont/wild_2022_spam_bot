#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc


class Header():
    def __init__(self):
        self.menu = dbc.Navbar(
            children = [
                dbc.NavItem("Spam Detect", className='nav-text'),
                dbc.NavItem(
                    dbc.DropdownMenu(
                        label="Présentation du project",
                        children=[
                            dbc.DropdownMenuItem("Les données d'entrées", href= '/presentation_du_projet/donnee_entree'),
                            dbc.DropdownMenuItem("Les algorithmes", href = '/presentation_du_projet/algorithme'),
                            dbc.DropdownMenuItem("Les performances", href = '/presentation_du_projet/performance'),
                        ],
                        nav=True,
                        in_navbar=True,
                    )
                ),

                dbc.NavItem(
                    dbc.NavLink(
                        "Detection des spams",
                        href='/detection_des_spams'
                    )
                ),
            ],
            color="primary",
            dark=True,
        )