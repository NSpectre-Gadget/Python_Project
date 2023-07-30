def total_wt_of_order():
    widget_wt = 75
    gizmo_wt = 112

    number_of_widgets = int(input("Enter the number of widgets in this order: "))
    number_of_gizmos = int(input("Enter the number of gizmos in this order: "))

    ttl_weight_widgets = number_of_widgets * widget_wt
    ttl_weight_of_gizmos = number_of_gizmos * gizmo_wt

    ttl_wt_of_order = ttl_weight_widgets + ttl_weight_of_gizmos

    print(
        f"The number of widgets ordered is {number_of_widgets} and the number of gizmos is {number_of_gizmos} and the total weight of the combined order is ${ttl_wt_of_order: .02f}"
    )


total_wt_of_order()
