class MetaArgs:
    """## Return:  meta data"""

    cost_of_goods_sold = """[Τεκμηρίωση cost_of_goods_sold]
[Βασικό στοιχείο που επηρεάζει τα μικτά αποτελέσματα της χρήσης είναι το κόστος των πωληθέντων αποθεμάτων.]
[Το κόστος πωλήσεων περιλαμβάνει τη διαφορά μεταξύ των κονδυλίων «κύκλος εργασιών» και «μικτά αποτελέσματα εκμεταλλεύσεως».   ]\n[Documentation cost_of_goods_sold]
[A key factor affecting the mixed results for the year is the cost of inventory sold. ]
[Cost of sales includes the difference between 'turnover' and 'gross operating results]'."""
    average_stock = """[Τεκμηρίωση average_stock]
[Το μέσο απόθεμα ανέρχεται στο μισό του μέγιστου αποθέματος ( [παραγωγή ανά ημέρα - ζήτηση ανά ημέρα] χ περίοδος παραγωγής σε ημέρες).]
[Documentation average_stock]\n[The average inventory is half of the maximum inventory ( [production per day - demand per day] x production period in days).          ]
"""
    sale_on_credit = """[Τεκμηρίωση sale_on_credit]\n[Παραστατικό πώλησης επί πιστώσει είναι ένα παραστατικό - τιμολόγιο - απόδειξη που εκδίδει μία επιχείρηση όταν αγοράζουν από αυτήν προϊόντα ή υπηρεσίες, που υποδηλώνει ότι θα πληρωθούν στο μέλλον με δόσεις.]
[Είναι δηλαδή ένα είδος πίστωσης που παρέχει στους πελάτες της, ώστε να τους διευκολύνει να μην πληρώσουν άμεσα τα χρήματα που απαιτούνται, αλλά με δόσεις, στο μέλλον. ]
[Documentation sale_on_credit]\n[A credit sales document is a document - invoice - receipt issued by a business when they buy products or services from it, indicating that they will be paid in the future in installments.]
[That is, it is a type of credit that it provides to its customers, in order to make it easier for them not to pay the money required immediately, but in installments, in the future.]
"""
    average_requirement = """[Τεκμηρίωση average_requirement]\n[Οι απαιτήσεις γενικά δημιουργούνται μέσω των πωλήσεων αποθεμάτων μιας επιχείρησης,]
[παρακολουθούνται μέσω των λογαριασμών όπως  Πελάτες αλλά κύριος από Γραμμάτια Εισπρακτέα, επιταγές Εισπρακτέες που διαθέτουν μια προκαθορισμένη προθεσμία εξόφλησής.]
[Συμφωνά με την βιβλιογραφία απαίτησης μπορούν να εμφανίζονται και σε προς τρίτους και όσο  και παροχές προσωπικού παροχή πίστωσης.]
[Κατά συνέπια τον παραπάνω το μεσώ απαιτήσεις είναι Μέσος Όρος των   απαιτήσεων μια συγκεκριμένης περιόδου. ]
[Documentation average_requirement]
[Receivables are generally created through a business's sales of inventory, tracked through accounts such as Accounts Payable but principal from Notes Receivable, checks Receivable that have a predetermined maturity date.]
[According to the claim literature they can appear in third party and personal benefits credit provision. As a result of the above, the average requirements is the average of the requirements of a certain period.]
"""
    medium_term_short_term_liabilities = """[Τεκμηρίωση medium_term_short_term_liabilities]
[Βραχυπρόθεσμες υποχρεώσεις είναι εκείνες για τις ποίες η προθεσμία εξοφλήσεώς τους λήγει μέχρι το τέλος της επόμενης χρήσεως και Αποτελούν Έξοδο για την επιχείρηση.]
[Κατά συνέπια τον παραπάνω  εδώ αναφερόμαστε Μέσος Όρος των Βραχυπρόθεσμων υποχρεώσεων  μια συγκεκριμένης περιόδου.]
[Documentation medium_term_short_term_liabilities]
[Short-term liabilities are those for which their repayment term expires by the end of the next fiscal year and constitute an Outgo for the business.]
[As a result of the above, here we refer to the Average Term of the Short-term obligations of a specific period.]
"""
    sourcing = """[Τεκμηρίωση sourcing]
[Αγορές που περιλαμβάνονται όπως αυτές αιτημάτων προϊόντων για μεταπώληση, άλλα και για παραγωγή σε ημιτελών προϊόντων, πρώτες ύλες , βοηθητικές ύλες.]
[Documentation sourcing]
[Purchases included such as those of product requests for resale, others and for production of unfinished products, raw materials, auxiliary materials.]
"""
    net_working_capital = """[Τεκμηρίωση net_working_capital]
[Καθαρό κεφάλαιο κίνησης είναι η διαφορά ανάμεσα στο κυκλοφορούν Ενεργητικό και τις βραχυπρόθεσμες Υποχρεώσεις]
[Documentation net_working_capital]
[Net working capital is the difference between current Assets and current Liabilities]
"""
    net_sales = """[Τεκμηρίωση net_sales]
[Η αξία των πωλήσεων μιας οικονομικής μονάδας μετά την αφαίρεση των φόρων (πχ. ΦΠΑ), των επιστροφών, των εκπτώσεων και της αξίας των κατεστραμμένων προϊόντων]
[Documentation net_sales]
[The value of sales of an economic unit after deduction of taxes (e.g. VAT), returns, discounts and the value of damaged products]
"""
    total_assets = """[Τεκμηρίωση total_assets]
[Εξετάζοντας τα περιουσιακά στοιχεία του Ενεργητικού διαπιστώνουμε ότι:]
[Μερικά από αυτά, όπως είναι οικόπεδα, κτίρια, μηχανήματα, μεταφορικά μέσα, έπιπλα και λοιπός εξοπλισμός, διπλώματα ευρεσιτεχνίας κτλ.]
[αποτελούν μόνιμο εξοπλισμό της επιχείρησης και προορίζονται να την εξυπηρετούν για χρονικό διάστημα μεγαλύτερο του έτους. Αυτά λέγονται Πάγια.]
[Άλλα περιουσιακά στοιχεία του Ενεργητικού, όπως είναι πελάτες, πρώτες και βοηθητικές ύλες, έτοιμα, προϊόντα, χρεόγραφα, γραμμάτια εισπρακτέα, ταμείο κτλ.]
[προορίζονται να υφίστανται συνεχείς μεταβολές στη διάρκεια της χρονιάς, π.χ. η πρώτη ύλη γίνεται έτοιμο προϊόν, το έτοιμο προϊόν μετρητά, τα μετρητά πρώτη ύλη κτλ.]
[Αυτά λέγονται Κυκλοφορούντα ή Κυκλοφοριακά.]
[Documentation total_assets]
[Examining the assets of the Asset we find that:]
[Some of them, such as land, buildings, machinery, means of transport, furniture and other equipment, patents, etc.]
[are permanent equipment of the company and are intended to serve it for a period longer than a year. This is what you call a fixed asset]
[Other assets of the Assets, such as customers, raw and auxiliary materials, finished products, securities, notes receivable, cash, etc.]
[are intended to undergo continuous changes during the year, e.g. raw material becomes finished product, finished product becomes cash, cash becomes raw material, etc.]
[This is what you call Current Assets]
"""
    net_assets = """[Τεκμηρίωση net_assets]
[Η καθαρή θέση επιχείρησης, επίσης γνωστή ως καθαρό ενεργητικό ή ίδια κεφάλαια, είναι η διαφορά μεταξύ του συνολικού ενεργητικού μιας εταιρείας και του συνολικού παθητικού της.]
[Αντιπροσωπεύει το εναπομένον ιδιοκτησιακό μερίδιο στα περιουσιακά στοιχεία της εταιρείας μετά την αφαίρεση όλων των υποχρεώσεών της.]
[Documentation net_assets]
[Business equity, also known as net assets or equity, is the difference between a company's total assets and its total liabilities.]
[It represents the remaining ownership stake in the company's assets after deducting all of its liabilities.]
"""
    invested_capital = """[Τεκμηρίωση invested_capital]
[Είναι το σύνολο των  κεφάλαιον που έχει επενδυθεί στην επιχείρηση, συμπεριλαμβανομένων των ιδίων κεφαλαίων και του μακροπρόθεσμων υποχρεώσεων (χρέος σε τρίτους).]
[Documentation invested_capital]
[It is the total amount of capital that has been invested in the business, including equity and long-term liabilities (debt to third parties).]
"""
    net_profit = """[Τεκμηρίωση net_profit]
[Στις επιχειρήσεις, το καθαρό εισόδημα ή τα καθαρά κέρδη είναι τα έσοδα μείον το κόστος πωληθέντων αγαθών, τα έξοδα και τους φόρους για μια λογιστική χρήση.]
[Documentation net_profit]
[In business, net income or net profit is revenue minus cost of goods sold, expenses, and taxes for an accounting year.]
"""
