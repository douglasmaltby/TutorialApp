//
// TutorialApp
//
// Created by SAP Cloud Platform SDK for iOS Assistant application on 08/03/20
//

import Foundation

enum Comsapedmsampleservicev2CollectionType: String {
    case customers = "Customers"
    case stock = "Stock"
    case products = "Products"
    case suppliers = "Suppliers"
    case purchaseOrderHeaders = "PurchaseOrderHeaders"
    case purchaseOrderItems = "PurchaseOrderItems"
    case salesOrderHeaders = "SalesOrderHeaders"
    case productCategories = "ProductCategories"
    case salesOrderItems = "SalesOrderItems"
    case productTexts = "ProductTexts"
    case none = ""
    static let all = [customers, stock, products, suppliers, purchaseOrderHeaders, purchaseOrderItems, salesOrderHeaders, productCategories, salesOrderItems, productTexts]
}
