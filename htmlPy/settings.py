ENABLE = 1
DISABLE = 0
INPUTS_ONLY = 2

RIGHT_CLICK_SETTING_KEY = "RIGHT_CLICK"
RIGHT_CLICK_ENABLE = "document.oncontextmenu = null;"
RIGHT_CLICK_DISABLE = "document.oncontextmenu = function(e) { return false; };"
RIGHT_CLICK_INPUTS_ONLY = "document.oncontextmenu = function(e) {" + \
    "return e.target.nodeName == 'INPUT' || e.target.nodeName == 'TEXTAREA'};"

TEXT_SELECTION_SETTING_KEY = "TEXT_SELECTION"
TEXT_SELECTION_ENABLE = "document.onselectstart = null;" + \
    "document.body.style.webkitUserSelect = '';" + \
    "document.body.style.cursor = '';"
TEXT_SELECTION_DISABLE = "document.onselectstart = function(e) " + \
    "{ return false; }; document.body.style.webkitUserSelect = 'none';" + \
    "document.body.style.cursor = 'default';"
