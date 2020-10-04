screen_helper = """
ScreenManager:
    StartScreen:
    HomeScreen:
    NewsScreen:
    VizScreen:
    ContactScreen:
<StartScreen>:
    name: 'start'
    BoxLayout:
        orientation: 'vertical'
        Image:
            spacing : "8dp"
            padding : "8dp"
            source : "Sansaar_Logo.jpg"
            size: self.texture_size
<HomeScreen>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Welcome'
            elevation:10
            MDIconButton:
                icon: "language-python"
                pos_hint: {"center_x": 0.95, "center_y": 0.5}
                on_release: app.navigate()
                user_font_size: "32sp"
                theme_text_color: 'ContrastParentBackground'
        MDLabel:
            text: 'We, the passionate adventurers of Team Sansaar, have worked with so much admiration through the NASA SpaceApps Challenge of 2020 in visualizing what nature has given and is giving us at each second of our lives. We believe that there is no PLANET B, atleast as of now, But the clock is ticking. It’s already late so let’s realize, what we are doing in reviving our planet EARTH.'
            halign: 'center'
            

        MDBottomAppBar:

            MDToolbar:
                icon: 'language-python'
                type: 'bottom'
                on_action_button: root.manager.current = 'vis'
                MDIconButton:
                    icon: "language-python"
                    on_release: root.manager.current = 'contact' 
                    user_font_size: "32sp"
                    theme_text_color: 'ContrastParentBackground'
        MDIconButton:
            icon: "language-python"
            pos : (0.9,0)
            on_release: root.manager.current = 'news'
            user_font_size: "32sp"
            theme_text_color: 'ContrastParentBackground'
<NewsScreen>:
    name: 'news'
    Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'News'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    Widget:
                    
                    
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "Sansaar_Logo.jpg"
                MDLabel:
                    text: "Let's save the Earth"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "and lets do it together"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                ScrollView:
                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Home"
                                on_release: root.manager.current = 'home' 
                                on_release: nav_drawer.toggle_nav_drawer()
                                IconLeftWidget:
                                    icon: "logout"



                            OneLineIconListItem:
                                text: "Analyze"
                                on_release: root.manager.current = 'vis' 
                                on_release: nav_drawer.toggle_nav_drawer() 
                                IconLeftWidget:
                                    icon: "upload"   

                            OneLineIconListItem:
                                text: "Community"
                                on_release: app.navigate() 
                                on_release: nav_drawer.toggle_nav_drawer()
                                IconLeftWidget:
                                    icon: "logout"


                            OneLineIconListItem:
                                text: "News"
                                on_release: root.manager.current = 'news' 
                                on_release: nav_drawer.toggle_nav_drawer()
                                IconLeftWidget:
                                    icon: "logout"


                            OneLineIconListItem:
                                text: "Contact Us"
                                on_release: root.manager.current = 'contact' 
                                on_release: nav_drawer.toggle_nav_drawer()
                                IconLeftWidget:
                                    icon: "logout"
<VizScreen>:
    name: 'vis'
    Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Analyse'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "Sansaar_Logo.jpg"
                MDLabel:
                    text: "Let's save the Earth"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "and lets do it together"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                ScrollView:
                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Home"
                                on_release: root.manager.current = 'home' 
                                on_release: nav_drawer.toggle_nav_drawer()
                                IconLeftWidget:
                                    icon: "logout"



                            OneLineIconListItem:
                                text: "Analyze"
                                on_release: root.manager.current = 'vis' 
                                on_release: nav_drawer.toggle_nav_drawer() 
                                IconLeftWidget:
                                    icon: "upload"   

                            OneLineIconListItem:
                                text: "Community"
                                on_release: app.navigate()
                                on_release: nav_drawer.toggle_nav_drawer()
                                IconLeftWidget:
                                    icon: "logout"


                            OneLineIconListItem:
                                text: "News"
                                on_release: root.manager.current = 'news' 
                                on_release: nav_drawer.toggle_nav_drawer()
                                IconLeftWidget:
                                    icon: "logout"


                            OneLineIconListItem:
                                text: "Contact Us"
                                on_release: root.manager.current = 'contact' 
                                on_release: nav_drawer.toggle_nav_drawer()
                                IconLeftWidget:
                                    icon: "logout"                                   
<ContactScreen>:
    name: 'contact'
    Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Contact Us'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    Widget:
                    Image:
                        padding: "4dp"
                        spacing: "4dp"
                        id: avatar
                        size_hint: (3.5,3.5)
                        pos_hint: {'center_x':0.5,'center_y':0}
                        source: "Sansaar.png"
                    MDLabel :
                        text : "       "
                    MDLabel :
                        text : "We did and will continuously work through odds to save our home planet. If you're interested, you can reach out to us on any of the given E-mails."
                        halign :'center'
                    MDLabel :
                        text : "      "
                    MDLabel :
                        text : "Anisha : Iamanisharastogi@gmail.com"
                        halign :'center'
                    MDLabel :
                        text : "Adhitya : adhityashreyas.p@gmail.com"
                        halign :'center'
                    MDLabel :
                        text : "Renuka : renukavelu17@gmail.com"
                        halign :'center'
                    MDLabel :
                        text : "Amaria : amariabonsi@gmail.com"
                        halign :'center'
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "Sansaar_Logo.jpg"
                MDLabel:
                    text: "Let's save the Earth"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "and lets do it together"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                ScrollView:
                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Home"
                                on_release: root.manager.current = 'home' 
                                on_release: nav_drawer.toggle_nav_drawer()
                                IconLeftWidget:
                                    icon: "logout"



                            OneLineIconListItem:
                                text: "Analyze"
                                on_release: root.manager.current = 'vis' 
                                on_release: nav_drawer.toggle_nav_drawer() 
                                IconLeftWidget:
                                    icon: "upload"   

                            OneLineIconListItem:
                                text: "Community"
                                on_release: app.navigate()
                                on_release: nav_drawer.toggle_nav_drawer()
                                IconLeftWidget:
                                    icon: "logout"


                            OneLineIconListItem:
                                text: "News"
                                on_release: root.manager.current = 'news' 
                                on_release: nav_drawer.toggle_nav_drawer()
                                IconLeftWidget:
                                    icon: "logout"


                            OneLineIconListItem:
                                text: "Contact Us"
                                on_release: root.manager.current = 'contact' 
                                on_release: nav_drawer.toggle_nav_drawer()
                                IconLeftWidget:
                                    icon: "logout"                   

"""