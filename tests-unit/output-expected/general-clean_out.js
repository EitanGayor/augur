exports.drive = (m) => {

    m.literal({"type":"literal","location":{"fileName":"test.js","pos":{"start":[1,1],"end":[4,3]}}});

    m.pop({"type":"expr","location":{"fileName":"test.js","pos":{"start":[1,1],"end":[4,3]}}});

    m.initVar("exports", {"type":"declaration","location":{"fileName":"test.js","pos":{"start":[1,2],"end":[4,2]}},"name":"exports"});

    m.initVar("require", {"type":"declaration","location":{"fileName":"test.js","pos":{"start":[1,2],"end":[4,2]}},"name":"require"});

    m.initVar("module", {"type":"declaration","location":{"fileName":"test.js","pos":{"start":[1,2],"end":[4,2]}},"name":"module"});

    m.initVar("__filename", {"type":"declaration","location":{"fileName":"test.js","pos":{"start":[1,2],"end":[4,2]}},"name":"__filename"});

    m.initVar("__dirname", {"type":"declaration","location":{"fileName":"test.js","pos":{"start":[1,2],"end":[4,2]}},"name":"__dirname"});

    m.initVar("a", {"type":"declaration","location":{"fileName":"test.js","pos":{"start":[1,2],"end":[4,2]}},"name":"a"});

    m.initVar("z", {"type":"declaration","location":{"fileName":"test.js","pos":{"start":[1,2],"end":[4,2]}},"name":"z"});

    m.literal({"type":"literal","location":{"fileName":"test.js","pos":{"start":[1,72],"end":[1,73]}}});

    m.writeVar("a", {"type":"variable","location":{"fileName":"test.js","pos":{"start":[1,68],"end":[1,73]}},"name":"a"});

    m.pop({"type":"expr","location":{"fileName":"test.js","pos":{"start":[1,68],"end":[1,73]}}});

    m.literal({"type":"literal","location":{"fileName":"test.js","pos":{"start":[2,11],"end":[2,12]}}});

    m.writeVar("z", {"type":"variable","location":{"fileName":"test.js","pos":{"start":[2,7],"end":[2,12]}},"name":"z"});

    m.pop({"type":"expr","location":{"fileName":"test.js","pos":{"start":[2,7],"end":[2,12]}}});

    m.endExecution();

};
