# OOjs UI license: https://github.com/wikimedia/oojs-ui/blob/master/LICENSE-MIT
# Everything else: public domain

import time  # Whoa.
import json

def pageRender(data):
    # Takes data and returns a static HTML page using OOjs UI
    # Page is returned as a string. A very long string.

    now = time.strftime("%c")

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

    page += 'var data = ' + json.dumps(data) + ';\n'
    page += 'var header = "<h1>NIOSH Wikidata Translation Report</h1><p>Last updated: ' + now + '</p><br />";\n'
    page += 'function rowGenerator( wikidataitem, language_code ) { \n'
    page += '  if (data[language_code]["wikidata"][wikidataitem] === null) { \n'
    page += '    this.tableButton = new OO.ui.ButtonWidget( {\n'
    page += '                           label: "Add Translation",\n'
    page += '                           href: "https://www.wikidata.org/wiki/Special:SetLabelDescriptionAliases/" + wikidataitem + "/" + language_code,\n'
    page += '                           target: "_blank",\n'
    page += '                           flags: [ "constructive" ],\n'
    page += '                           framed: false,\n'
    page += '                           icon: "add",\n'
    page += '                           classes: [ "inlineButton" ]\n'
    page += '                           } );\n'
    page += '    this.tableRow = "<tr class=missing><td>";'
    page += '    if (data["en"]["wikidata"][wikidataitem] != null) {\n'
    page += '      this.tableRow += data["en"]["wikidata"][wikidataitem];\n'
    page += '    } else {\n'
    page += '      this.tableRow += "—";\n'
    page += '    };\n'
    page += '    this.tableRow += "</td><td>→</td><td>missing</td><td class=btn></td></tr>";\n'
    page += '  } else {\n'
    page += '    this.tableButton = new OO.ui.ButtonWidget( {\n'
    page += '                           label: "Fix Translation",\n'
    page += '                           href: "https://www.wikidata.org/wiki/Special:SetLabelDescriptionAliases/" + wikidataitem + "/" + language_code,\n'
    page += '                           target: "_blank",\n'
    page += '                           flags: [ "progressive" ],\n'
    page += '                           framed: false,\n'
    page += '                           icon: "check",\n'
    page += '                           classes: [ "inlineButton" ]\n'
    page += '                           } );\n'
    page += '    this.tableRow = "<tr class=translated><td>";'
    page += '    if (data["en"]["wikidata"][wikidataitem] != null) {\n'
    page += '      this.tableRow += data["en"]["wikidata"][wikidataitem];\n'
    page += '    } else {\n'
    page += '      this.tableRow += "—";\n'
    page += '    };\n'
    page += '    this.tableRow += "</td><td>→</td><td>" + data[language_code]["wikidata"][wikidataitem] + "</td><td class=btn></td></tr>";\n'
    page += '  };\n'
    page += '  this.$element.find( ".btn" ).append( this.tableButton );\n'
    page += '};\n'

    for language_code, bundle in data.items():
        if language_code == 'en': # We don't generate a report in English
            continue

        block = "\n"  # Mark Block here
        
        block += "function " + language_code + "Layout( name, config ) {  \n"

        block += "  " + language_code + "Layout.super.call( this, name, config );\n"
        block += "  this.$element.append( header );\n"
    
        block += "  var progressBar = new OO.ui.ProgressBarWidget( {\n"
        block += "    progress: " + str(int(bundle['gap_analysis'] * 100)) + "\n"
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

        block += '  var ReportTable = "<table class=report></table>";\n'
        block += '  var ReportContent;\n'
        block += '  for (entry in data[language_code]["wikidata"]) {\n'
        block += '    var addition = new rowGenerator( entry, language_code );\n'
        block += '    ReportContent += addition.tableRow;\n'
        block += '  };\n'
        block += '  this.$element.find( ".report" ).append( ReportContent );\n'
        block += '};\n'

        page += block

    for language in data:
        if language != "en":  # Again, English does not have its own list
            page += "var page" + language + " = new " + language + "Layout( '" + language + "' );\n"

    page += '''
           var booklet = new OO.ui.BookletLayout( { 
             outlined: true
           } );
           '''

    list_of_pages = ""
    for language in language_labels:
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