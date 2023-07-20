/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ListX2ManyField } from "@web/views/fields/x2many/list_x2many_field";
import { useChildRef, useOwnedDialogs, useService } from "@web/core/utils/hooks";
const { Component,useRef,onWillUpdateProps,useState} = owl;

export class KanbanOne2ManyNamesField extends ListX2ManyField {
    static template = "KanbanOne2ManyNamesField";

    get items(){
        if (this.props.record.fields[this.props.name].type == "one2many"){
            const _items = this.props.record.preloadedData[this.props.name]
            console.log(_items)
            return _items;
        }else{
            return [];
        }
    }

}


export class TimetableLines extends KanbanOne2ManyNamesField {
    static template = "TimetableLines";
}

registry.category("fields").add("kanban_one2many_names", KanbanOne2ManyNamesField);
registry.category("fields").add("timetable_lines", TimetableLines);

export async function preloadOne2Many(orm, record, fieldName) {
    const field = record.fields[fieldName];
    const context = record.evalContext;
    const records = await orm.read(field.relation, context[fieldName]);
    return records;
}

registry.category("preloadedData").add("kanban_one2many_names", {
    loadOnTypes: ["one2many"],
    preload: preloadOne2Many,
});

registry.category("preloadedData").add("timetable_lines", {
    loadOnTypes: ["one2many"],
    preload: preloadOne2Many,
});