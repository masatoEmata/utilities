function getUniqueItems(duplicated_items) {
    var unique_ids = {}
    duplicated_items.map((x, i) => unique_ids[x.id] = i); //ユニークなキーをセット
    var unique_items = Object.values(unique_ids).map(x => duplicated_items[x])
    return unique_items
}

var duplicated_items = [
    { id: "1111", name: "item1" },
    { id: "2222", name: "item2" },
    { id: "1111", name: "item1" },
    { id: "3333", name: "item3" },
];

getUniqueItems(duplicated_items)