# OOjs UI license: https://github.com/wikimedia/oojs-ui/blob/master/LICENSE-MIT
# Everything else: public domain


def pageRender(manifest, gap_report, language_labels):
    # Takes data and returns a static HTML page using OOjs UI
    # Page is returned as a string. A very long string.

    page = '''
           <!DOCTYPE html>
           <html lang="en" dir="ltr">
           <head>
           <meta charset="UTF-8">
           <title>NIOSH Wikidata Translation Report</title>
           <meta name="viewport" content="width=device-width, user-scalable=no">
           <link rel="stylesheet" type="text/css" href="node_modules/oojs-ui/dist/oojs-ui-mediawiki.css" />
           <style type="text/css">
           body {
               font-family: 'Helvetica Neue', sans-serif;
           }
           h1 {
               margin-top:0;
           }
           #progress {
               margin-top:5px;
           }
           .oo-ui-progressBarWidget-bar {
               background: #347bff;
           }
           .inlineButton {
               font-size: 95%;
           }
           table {
               padding-top:2em;
           }
           td {
               padding:5px;
           }
           tr.missing td:nth-child(3) {
               color: #aaa;
               font-style: italic;
           }
           </style>
           </head>
           <body>
           <script src="node_modules/oojs-ui/node_modules/jquery/dist/jquery.js"></script>
           <script src="node_modules/oojs-ui/node_modules/es5-shim/es5-shim.js"></script>
           <script src="node_modules/oojs-ui/node_modules/oojs/dist/oojs.jquery.js"></script>
           <script src="node_modules/oojs-ui/dist/oojs-ui.js"></script>
           <script src="node_modules/oojs-ui/dist/oojs-ui-mediawiki.js"></script>
           <script>


           '''

    for language, collection in manifest.items():
        if language == 'en': # We don't generate a report in English
            continue

        block = "\n"  # Mark Block here
        
        block += "function " + language + "Layout( name, config ) {  \n"

        block += "  " + language + "Layout.super.call( this, name, config );\n"
        block += "  this.$element.append( '<h1>NIOSH Wikidata Translation Report</h1>' );\n"
    
        block += "  var progressBar = new OO.ui.ProgressBarWidget( {\n"
        block += "    progress: " + str(int(gap_report[language])) + "\n"
        block += "  } );\n"
    
        block += "  this.$element.append( progressBar.$element );\n"
        block += "  this.$element.append( '<p id=progress><b>' + progressBar.progress + '%</b> of terms are translated.</p>' );\n"
    
        block += "  var toggleSwitch1 = new OO.ui.ToggleSwitchWidget( { \n"
        block += "    value: false\n"
        block += "  } );"

        block += "  var that = this;\n"
        block += "  toggleSwitch1.on( 'change', function() {\n"
        block += "    that.$element.find( '.translated' ).toggle( !toggleSwitch1.getValue() );\n"
        block += "  } );\n"
    
        block += "  this.$element.append( '<div>' );\n"
        block += "  this.$element.append( toggleSwitch1.$element );\n"
        block += "  this.$element.append( '&nbsp; Only show missing translations</div>' );\n"

        buttonDefinitions = ""
        buttonCounter = 1

        for wikidataitem, label in collection.items():
            if label == None:  # Term needs to be translated
                button = ""
                button += "  var tableButton" + str(buttonCounter) + " = new OO.ui.ButtonWidget( {\n"
                button += "    label: 'Add Translation',\n"
                button += "    href: 'https://www.wikidata.org/wiki/Special:SetLabelDescriptionAliases/" + wikidataitem + "/" + language + "',\n"
                button += "    target: '_blank',\n"
                button += "    flags: [ 'constructive' ],\n"
                button += "    framed: false,\n"
                button += "    icon: 'add',\n"
                button += "    classes: [ 'inlineButton' ]"
                button += "  } );\n"
                button += "  var Row" + str(buttonCounter) + " = '<tr class=missing><td>"
                button += manifest['en'][wikidataitem] + "</td><td>→</td><td>missing</td><td class=placeholder"
                button += str(buttonCounter) + "></td></tr>';\n"
            else:  # Term has already been translated
                button = ""
                button += "  var tableButton" + str(buttonCounter) + " = new OO.ui.ButtonWidget( {\n"
                button += "    label: 'Fix Translation',\n"
                button += "    href: 'https://www.wikidata.org/wiki/Special:SetLabelDescriptionAliases/" + wikidataitem + "/" + language + "',\n"
                button += "    target: '_blank',\n"
                button += "    flags: 'progressive',\n"
                button += "    framed: false,\n"
                button += "    icon: 'check',\n"
                button += "    classes: [ 'inlineButton' ]\n"
                button += "  } );\n"
                button += "  var Row" + str(buttonCounter) + " = '<tr class=translated><td>"
                button += manifest['en'][wikidataitem] + "</td><td>→</td><td>" + label
                button += "</td><td class=placeholder" + str(buttonCounter) + "></td></tr>';\n"

            block += button
            buttonCounter += 1

        block += "  var TableStart = '<table>';\n"
        block += "  var TableEnd = '</table>';\n"

        block += "  this.$element.append( TableStart + "
        for x in range(1, buttonCounter):
            block += "Row" + str(x) + " + "
        block += "TableEnd );\n"

        for x in range(1, buttonCounter):  # Yes, this again
            block += "  this.$element.find( '.placeholder" + str(x) + "' ).append( tableButton" + str(x) + ".$element );\n"

        block += "  OO.inheritClass( " + language + "Layout, OO.ui.PageLayout );\n"
        block += "  " + language + "Layout.prototype.setupOutlineItem = function () {\n"
        block += "    this.outlineItem.setLabel( '" + language_labels[language] + "' );\n"
        block += "  };\n"

        page += block

    for version in language_labels:
        if version == "en":  # Again, English does not have its own list
            continue

        page += "var page" + language + " = new " + language + "Layout( '" + language + "' );\n"

    page += '''
           var booklet = new OO.ui.BookletLayout( { 
             outlined: true
           } );
           '''

    list_of_pages = ""
    for language in manifest:
        if language != "en":
            list_of_pages += "page" + language + ", "
    list_of_pages = list_of_pages[:-2]

    page += "booklet.addPages ( [ " + list_of_pages + " ] );\n"

    # And finally...

    page += '''
            $( 'body' ).append( booklet.$element );
            </script>
            </body>
            </html>
            '''


    return page