async function loadWorkspace() {
    const response = await fetch("/data");
    const json = await response.json();
    const table = await perspective.worker().table(json);

    const workspace = document.getElementById("workspace");
    await workspace.restore({
        detail: {
            tables: {
                "Main": table
            }
        }
    });

    // Load a default panel
    workspace.add_panel({
        type: "DATAGRID",
        table: "Main",
        title: "Editable Table",
        editable: true
    });
}

loadWorkspace();