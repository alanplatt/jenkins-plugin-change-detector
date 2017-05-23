#!/usr/bin/env python
from jenkins_plugin_change_detector.html_loader import (get_HTML_doc, parse_HTML,
                                                        get_confluence_table_from_HTML_object,
                                                        get_release_date_from_confluenceTable_object)

def main():
    html = get_HTML_doc("https://wiki.jenkins-ci.org/display/JENKINS/Workspace+Cleanup+Plugin")
    html_object = parse_HTML(html)
    table_object = get_confluence_table_from_HTML_object(html_object)
    print get_release_date_from_confluenceTable_object(table_object)


if __name__ == "__main__":
    main()
