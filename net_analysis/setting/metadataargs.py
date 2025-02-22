class MetaArgs:
    """Documentation args"""
    
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
    circulating_assets = """[Τεκμηρίωση circulating_assets]
[Κυκλοφορούντα Περιουσιακά στοιχεία αποτελούν τα περιουσιακά στοιχεία του Ενεργητικού που προορίζονται να αλλάζουν θέση και μορφή μία ή περισσότερες φορές μέσα σε μια διαχειριστική χρήση (ένα έτος).]
[Τα κυκλοφορούντα περιουσιακά στοιχεία διακρίνονται σε:]
[Αποθέματα υλικών αξιών, όπως εμπορεύματα, έτοιμα προϊόντα, ημιτελή προϊόντα, πρώτες και βοηθητικές ύλες, ανταλλακτικά πάγιων στοιχείων, είδη συσκευασίας κτλ. Βραχυπρόθεσμες απαιτήσεις.]
[Είναι οι απαιτήσεις που πρόκειται να εισπραχθούν το αργότερο μέχρι το τέλος της επόμενης χρήσης, όπως πελάτες, γραμμάτια εισπρακτέα, χρεώστες διάφοροι κτλ. Χρεόγραφα.]
[Είναι οι μετοχές Α.Ε. (εφόσον δεν πρόκειται για συμμετοχές), ομολογίες, ομόλογα, έντοκα γραμμάτια του Ελληνικού Δημοσίου, κτλ. Διαθέσιμα.]
[Είναι τα περιουσιακά στοιχεία που μετατρέπονται σε χρήματα αμέσως και ασφαλώς, δηλαδή μπορούν να χρησιμοποιηθούν για πληρωμές σε οποιαδήποτε στιγμή, όπως μετρητά (ταμείο), καταθέσεις όψεως, ληγμένα τοκομερίδια ομολογιών εισπρακτέα.]
[Το κόστος πωλήσεων περιλαμβάνει τη διαφορά μεταξύ των κονδυλίων «κύκλος εργασιών» και «μικτά αποτελέσματα εκμεταλλεύσεως».   ]
[Documentation circulating_assets]
Current Assets are the assets of the Asset that are intended to change position and one or more times within a management year (one year).]
[Current assets are divided into: Inventories of tangible assets, such as merchandise, finished products, unfinished products, raw and auxiliary materials, spare parts of fixed assets, types of packaging, etc.]
[Short term receivables. These are the receivables that are to be collected by the end of the next fiscal year at the latest, such as customers, notes receivable, miscellaneous debtors, etc.]
[Securities. Are the shares of A.E. (as long as it is not about participations), bonds, bonds, interest-bearing bonds of the Greek State, etc.]
[available_cash. They are the assets that can be converted into money immediately and safely, that is, they can be used for payments at any time, such as cash (cash), demand deposits, maturing notes receivable.]"""

    short_term_liabilities = """[Τεκμηρίωση short_term_liabilities]
[Βραχυπρόθεσμες υποχρεώσεις είναι εκείνες για τις ποίες η προθεσμία εξοφλήσεώς τους λήγει μέχρι το τέλος της επόμενης χρήσεως και Αποτελούν Έξοδο για την επιχείρηση.]
[Documentation short_term_liabilities]
[Short-term liabilities are those for which their repayment term expires by the end of the next fiscal year and constitute an Outgo for the business.]
"""

    available_cash = """[Τεκμηρίωση available_cash]
[Είναι τα περιουσιακά στοιχεία που μετατρέπονται σε χρήματα αμέσως και ασφαλώς, δηλαδή μπορούν να χρησιμοποιηθούν για πληρωμές σε οποιαδήποτε στιγμή, όπως μετρητά (ταμείο), καταθέσεις όψεως, ληγμένα τοκομερίδια ομολογιών εισπρακτέα.]
[Documentation available_cash]
[They are the assets that can be converted into money immediately and safely, that is, they can be used for payments at any time, such as cash (cash), demand deposits, maturing notes receivable.]
"""
    stock = """[Τεκμηρίωση stock]
[Το  μέγιστου αποθέματος μια συγκεκριμένης ημέρας στην αποθήκη.]
[Documentation average_stock]
[The maximum stock of a particular day in the warehouse).          ]
"""

    forecast_daily_expenses = """[Τεκμηρίωση forecast_daily_expenses]
[αναφέρεται στην εκτίμηση ή πρόβλεψη των ημερήσιων δαπανών με βάση τα ιστορικά δεδομένα, πρότυπα των δαπανών, και τις αναμενόμενες μελλοντικές ανάγκες.]
[Αυτό συνήθως περιλαμβάνει την ανάλυση παρελθόν έξοδα, την κατηγοριοποίηση των δαπανών, και τον υπολογισμό των μέσων όρων ή τάσεις να προβλέψει το μέλλον της καθημερινής κόστος]
[Documentation forecast_daily_expenses]
[refers to the estimation or prediction of daily spending based on historical data, spending patterns, and expected future needs.]
[It typically involves analyzing past expenses, categorizing expenditures, and calculating averages or trends to anticipate future daily costs.]
"""

    requirements = """[Τεκμηρίωση requirements]
[Στα οικονομικά και τη λογιστική, ο όρος "requirements" αναφέρεται σε:]
[Πόρους, κεφάλαια ή αγαθά που είναι απαραίτητα για την επίτευξη ενός στόχου, την υλοποίηση ενός έργου ή τη διατήρηση της λειτουργίας μιας επιχείρησης.]
[Στην περίπτωση επιχειρήσεων, περιλαμβάνει συχνά χρηματοοικονομικές απαιτήσεις]
[όπως εισπρακτέα ποσά από πελάτες (accounts receivable) ή άλλα στοιχεία που σχετίζονται με τον κύκλο εργασιών.]
[Documentation requirements]
[Requirements refer to the necessary resources, funds, or goods needed to achieve a goal, execute a project, or maintain a business's operations.]
[In financial terms, it often includes receivables or other obligations linked to the operating cycle]
"""

class MetaEquityCapital:
    """## Documentation args"""

    net_profit = """[Τεκμηρίωση net_profit]
[Στις επιχειρήσεις, το καθαρό εισόδημα ή τα καθαρά κέρδη είναι τα έσοδα μείον το κόστος πωληθέντων αγαθών, τα έξοδα και τους φόρους για μια λογιστική χρήση.]
[Documentation net_profit]
[In business, net income or net profit is revenue minus cost of goods sold, expenses, and taxes for an accounting year.]
"""
    net_sales = """[Τεκμηρίωση net_sales]
[Η αξία των πωλήσεων μιας οικονομικής μονάδας μετά την αφαίρεση των φόρων (πχ. ΦΠΑ), των επιστροφών, των εκπτώσεων και της αξίας των κατεστραμμένων προϊόντων]
[Documentation net_sales]
[The value of sales of an economic unit after deduction of taxes (e.g. VAT), returns, discounts and the value of damaged products]
"""
    fixed_asset = """[Τεκμηρίωση assets]
[Εξετάζοντας τα περιουσιακά στοιχεία του Ενεργητικού διαπιστώνουμε ότι:]
[Μερικά από αυτά, όπως είναι οικόπεδα, κτίρια, μηχανήματα, μεταφορικά μέσα, έπιπλα και λοιπός εξοπλισμός, διπλώματα ευρεσιτεχνίας κτλ.]
[αποτελούν μόνιμο εξοπλισμό της επιχείρησης και προορίζονται να την εξυπηρετούν για χρονικό διάστημα μεγαλύτερο του έτους. Αυτά λέγονται Πάγια.]
[Documentation assets]
[Examining the assets of the Asset we find that:]
[Some of them, such as land, buildings, machinery, means of transport, furniture and other equipment, patents, etc.]
[are permanent equipment of the company and are intended to serve it for a period longer than a year. This is what you call a fixed asset]
"""
    equity_capital = """[Τεκμηρίωση equity_capital]
[Ίδια κεφάλαια (καθαρή περιουσιακή θέση) είναι ό,τι βρίσκεται στην κυριότητά σας εάν αφαιρέσετε διάφορες χρεώσεις που σας επιβαρύνουν ή τα χρήματα που δανειστήκατε για να το αγοράσετε.]
[Όταν επενδύετε, ίδια κεφάλαια είναι οι μετοχές που σας παρέχουν ένα μερίδιο κυριότητας σε μια εταιρεία.]
[Documentation equity_capital]
[Equity (net worth) is what you own if you subtract various charges you incur or money borrowed to buy.]
[When you invest, equity is the shares that give you an ownership stake in a company.]
"""


class MetaFinancialLeverageRadio:
    """## Return:  meta data"""

    net_profit = """[Τεκμηρίωση net_profit]
[Στις επιχειρήσεις, το καθαρό εισόδημα ή τα καθαρά κέρδη είναι τα έσοδα μείον το κόστος πωληθέντων αγαθών, τα έξοδα και τους φόρους για μια λογιστική χρήση.]
[Documentation net_profit]
[In business, net income or net profit is revenue minus cost of goods sold, expenses, and taxes for an accounting year.]
"""
    net_sales = """[Τεκμηρίωση net_sales]
[Η αξία των πωλήσεων μιας οικονομικής μονάδας μετά την αφαίρεση των φόρων (πχ. ΦΠΑ), των επιστροφών, των εκπτώσεων και της αξίας των κατεστραμμένων προϊόντων]
[Documentation net_sales]
[The value of sales of an economic unit after deduction of taxes (e.g. VAT), returns, discounts and the value of damaged products]
"""
    fixed_asset = """[Τεκμηρίωση assets]
[Εξετάζοντας τα περιουσιακά στοιχεία του Ενεργητικού διαπιστώνουμε ότι:]
[Μερικά από αυτά, όπως είναι οικόπεδα, κτίρια, μηχανήματα, μεταφορικά μέσα, έπιπλα και λοιπός εξοπλισμός, διπλώματα ευρεσιτεχνίας κτλ.]
[αποτελούν μόνιμο εξοπλισμό της επιχείρησης και προορίζονται να την εξυπηρετούν για χρονικό διάστημα μεγαλύτερο του έτους. Αυτά λέγονται Πάγια.]
[Documentation assets]
[Examining the assets of the Asset we find that:]
[Some of them, such as land, buildings, machinery, means of transport, furniture and other equipment, patents, etc.]
[are permanent equipment of the company and are intended to serve it for a period longer than a year. This is what you call a fixed asset]
"""
    equity_capital = """[Τεκμηρίωση assets]
[Ίδια κεφάλαια (καθαρή περιουσιακή θέση) είναι ό,τι βρίσκεται στην κυριότητά σας εάν αφαιρέσετε διάφορες χρεώσεις που σας επιβαρύνουν ή τα χρήματα που δανειστήκατε για να το αγοράσετε.]
[Όταν επενδύετε, ίδια κεφάλαια είναι οι μετοχές που σας παρέχουν ένα μερίδιο κυριότητας σε μια εταιρεία.]
[Documentation equity_capital]
[Equity (net worth) is what you own if you subtract various charges you incur or money borrowed to buy.]
[When you invest, equity is the shares that give you an ownership stake in a company.]
"""
    interest = """[Τεκμηρίωση interest]
[Τόκος είναι η αποζημίωση σε χρήματα που είναι υποχρεωμένος να δώσει ο οφειλέτης στο δανειστή για ορισμένη ποσότητα χρηματικού δανείου που πήρε για συγκεκριμένη χρονική περίοδο.]
[Οι οικονομολόγοι συχνά αναφέρονται στον τόκο ως αμοιβή για τη χρησιμοποίηση χρηματικού κεφαλαίου, ή ως τιμή με την οποία χρεώνεται η χρήση κεφαλαίου. Ο λόγος του τόκου προς το κεφάλαιο λέγεται επιτόκιο. ]
[Documentation interest]
[Interest is the compensation in money that the debtor is obliged to give to the lender for a certain amount of money borrowed for a certain period of time.]
[Economists often refer to interest as a fee for the use of money capital, or as the price at which the use of capital is needed. The ratio of the interest to the principal is called the interest rate.]
"""
    tax_rate = """[Τεκμηρίωση tax_rate]
[Ο φορολογικός συντελεστής (tax_rate) είναι ένα ποσοστό που αντιπροσωπεύει το ποσό του φόρου που επιβάλλεται στα κέρδη μιας επιχείρησης ή ενός ατόμου. Εκφράζεται συνήθως ως δεκαδικός αριθμός ή ποσοστό.]
[Documentation tax_rate]
[The tax rate (tax_rate) is a percentage that represents the amount of tax levied on the profits of a business or an individual. It is usually expressed as a decimal number or percentage.]
"""

class MetaGrossMargin:
    """## Return:  meta data
    arithmetical gross profit => Αριθμοδείκτης μικτού κέρδους
    """

    gross_operating_profit = """[Τεκμηρίωση gross_operating_profit]
[Το ακαθάριστο λειτουργικό κέρδος (ή Gross Operating Profit) αναφέρεται στο κέρδος που προκύπτει από τις λειτουργικές δραστηριότητες μιας επιχείρησης, πριν αφαιρεθούν τα λειτουργικά έξοδα, οι τόκοι, οι φόροι και άλλες εξωτερικές δαπάνες.]
[Στην ουσία, είναι το κέρδος που παράγεται από την κύρια δραστηριότητα της επιχείρησης, χωρίς να λαμβάνονται υπόψη οι μη λειτουργικές δραστηριότητες ή οι μη-λειτουργικές δαπάνες (όπως τα χρηματοοικονομικά έξοδα ή τα έκτακτα έξοδα).]
[Documentation gross_operating_profit]
[Gross Operating Profit (or Gross Operating Profit) refers to the profit obtained from the operating activities of a business, before deducting operating expenses, interest, taxes and other external costs.]
[In essence, it is the profit generated by the main activity of the business, without taking into account non-operating activities or non-operating expenses (such as financial expenses or extraordinary expenses).]
"""
    net_sales = """[Τεκμηρίωση net_sales]
[Η αξία των πωλήσεων μιας οικονομικής μονάδας μετά την αφαίρεση των φόρων (πχ. ΦΠΑ), των επιστροφών, των εκπτώσεων και της αξίας των κατεστραμμένων προϊόντων]
[Documentation net_sales]
[The value of sales of an economic unit after deduction of taxes (e.g. VAT), returns, discounts and the value of damaged products]
"""
    net_operating_profit = """[Τεκμηρίωση net_operating_profit]
[Το καθαρό λειτουργικό κέρδος (ή Net Operating Profit – NOP) αναφέρεται στο ποσό του κέρδους που απομένει από τις λειτουργικές δραστηριότητες μιας επιχείρησης αφού αφαιρεθούν όλα τα άμεσα και έμμεσα λειτουργικά έξοδα, εκτός από τους τόκους και τους φόρους.]
[Δηλαδή, είναι το κέρδος που έχει απομείνει αφού καλυφθούν οι δαπάνες που συνδέονται με την παραγωγή, τη διάθεση και τη διαχείριση των προϊόντων ή υπηρεσιών της επιχείρησης.]
[Documentation net_operating_profit]
[Net Operating Profit (or NOP) refers to the amount of profit remaining from the operating activities of a business after deducting all direct and indirect operating expenses, excluding interest and taxes.]
[That is, it is the profit that is left after covering the costs associated with the production, distribution and management of the company's products or services.]

"""
    sales = """[Τεκμηρίωση sales]
[Ο όρος "πώλησης" αναφέρεται στην πράξη της ανταλλαγής αγαθών ή υπηρεσιών για χρήματα ή άλλους πόρους. Στο οικονομικό και επιχειρηματικό πλαίσιο, η πώληση είναι μια βασική συναλλαγή που επιτρέπει στις επιχειρήσεις να παράγουν έσοδα και να λειτουργούν.]
[Η πώληση δεν περιορίζεται μόνο στην ανταλλαγή προϊόντων, αλλά μπορεί να περιλαμβάνει και την παροχή υπηρεσιών.]
[Documentation sales]
[The term "sale" refers to the act of exchanging goods or services for money or other resources. In the economic and business context, selling is a key transaction that allows businesses to generate revenue and operate.]
[Selling is not only limited to the exchange of products, but may also include the provision of services.]
"""
    net_profit_of_use = """[Τεκμηρίωση net_profit_of_use]
[Το καθαρό κέρδος χρήσης αναφέρεται στο καθαρό κέρδος που απομένει στην επιχείρηση μετά την αφαίρεση όλων των εξόδων λειτουργίας, φόρων, τόκων και άλλων υποχρεώσεων από τα έσοδα της επιχείρησης κατά τη διάρκεια μιας συγκεκριμένης χρήσης (χρηματοοικονομικής περιόδου).
[Αυτή η έννοια μπορεί να έχει διάφορους συνυπολογισμούς, ανάλογα με το τι περιλαμβάνει το "καθαρό" κέρδος, και συχνά συνδέεται με τον λογιστικό ορισμό του καθαρού κέρδους.]
[Documentation net_profit_of_use]
[Net profit for a year refers to the net profit left in the business after deducting all operating expenses, taxes, interest and other liabilities from the revenue of the business during a particular year (financial period).]
[Αυτή η έννοια μπορεί να έχει διάφορους συνυπολογισμούς, ανάλογα με το τι περιλαμβάνει το "καθαρό" κέρδος, και συχνά συνδέεται με τον λογιστικό ορισμό του καθαρού κέρδους.]
"""
    total_of_these_funds = """[Τεκμηρίωση total_of_these_funds]
[Το σύνολο θέσης κεφαλαίων αναφέρεται στο συνολικό ποσό κεφαλαίων που χρησιμοποιεί μια επιχείρηση ή ένας επενδυτής για να χρηματοδοτήσει τις δραστηριότητες ή τις επενδύσεις του.]
[Αυτό το ποσό μπορεί να περιλαμβάνει διάφορες πηγές χρηματοδότησης, όπως ιδία κεφάλαια, δανεισμό ή άλλες μορφές χρηματοδότησης.]
[Documentation total_of_these_funds]
[Total capital position refers to the total amount of capital that a business or investor has to finance its operations or investments.]
[This amount may include various sources of financing, such as equity, debt or other forms of financing.]
"""

class MetaMaintenanceRepair:
    """## Return:  meta data
    arithmetical gross profit => Αριθμοδείκτης μικτού κέρδους"""

    cost_of_goods_sold = """[Τεκμηρίωση cost_of_goods_sold]
[Βασικό στοιχείο που επηρεάζει τα μικτά αποτελέσματα της χρήσης είναι το κόστος των πωληθέντων αποθεμάτων.]
[Το κόστος πωλήσεων περιλαμβάνει τη διαφορά μεταξύ των κονδυλίων «κύκλος εργασιών» και «μικτά αποτελέσματα εκμεταλλεύσεως».   ]\n[Documentation cost_of_goods_sold]
[A key factor affecting the mixed results for the year is the cost of inventory sold. ]
[Cost of sales includes the difference between 'turnover' and 'gross operating results]'."""
    net_sales = """[Τεκμηρίωση net_sales]
[Η αξία των πωλήσεων μιας οικονομικής μονάδας μετά την αφαίρεση των φόρων (πχ. ΦΠΑ), των επιστροφών, των εκπτώσεων και της αξίας των κατεστραμμένων προϊόντων]
[Documentation net_sales]
[The value of sales of an economic unit after deduction of taxes (e.g. VAT), returns, discounts and the value of damaged products]
"""
    maintenance_and_repair_costs = """[Τεκμηρίωση maintenance_and_repair_costs]
Τα έξοδα συντήρησης και επισκευής (maintenance and repair costs) αναφέρονται σε εκείνα τα έξοδα που προκύπτουν για τη διατήρηση των πάγιων περιουσιακών στοιχείων ή των εγκαταστάσεων σε λειτουργική κατάσταση και την αποκατάσταση των τυχόν ζημιών ή φθορών που προκύπτουν από τη χρήση τους.]
[Αυτά τα έξοδα είναι συνήθως απαραίτητα για την καλή λειτουργία και μακροχρόνια διάρκεια ζωής των υποδομών, του εξοπλισμού και των μηχανημάτων.]
[Documentation maintenance_and_repair_costs]
[Maintenance and repair costs (maintenance and repair costs) refer to those costs incurred to maintain the fixed assets or facilities in an operational condition and to repair any damages or damages resulting from their use.]
[These costs are usually necessary for the good operation and long life of the infrastructure, equipment and machinery.]
"""
    fixed_assets_before_depreciation = """[Τεκμηρίωση fixed_assets_before_depreciation]
[Τα πάγια στοιχεία πριν από τις αποσβέσεις (fixed assets before depreciation) αναφέρονται στην αξία των πάγιων περιουσιακών στοιχείων μιας επιχείρησης πριν εφαρμοστούν οι αποσβέσεις. ]
[Τα πάγια στοιχεία περιλαμβάνουν τα υλικά ή άυλα περιουσιακά στοιχεία που χρησιμοποιούνται από την επιχείρηση για μεγαλύτερο χρονικό διάστημα, συνήθως πάνω από 1 έτος, και δεν προορίζονται για άμεση πώληση.]
[Documentation fixed_assets_before_depreciation]
[Fixed assets before depreciation refer to the value of a company's fixed assets before depreciation is applied.]
[Fixed assets include tangible or intangible assets that are used by the business for a longer period of time, usually more than 1 year, and are not intended for immediate sale.]
"""
    depreciation_of_use = """[Τεκμηρίωση depreciation_of_use]
[Η απόσβεση χρήσης (depreciation of use) αναφέρεται στον τρόπο με τον οποίο ένα πάγιο περιουσιακό στοιχείο χάνει την αξία του με την πάροδο του χρόνου, λόγω της χρήσης του στην παραγωγική διαδικασία ή στις καθημερινές λειτουργίες της επιχείρησης.]
[Η συγκεκριμένη φράση τονίζει τη συσχέτιση της απόσβεσης με την ένταση και διάρκεια χρήσης του περιουσιακού στοιχείου.]
[Documentation depreciation_of_use]
[Depreciation of use refers to the way in which a fixed asset loses its value over time, due to its use in the production process or in the day-to-day operations of the business.]
[This phrase emphasizes the correlation of depreciation with the intensity and duration of use of the asset.]
"""
    fixed_assets_for_depreciation = """[Τεκμηρίωση fixed_assets_for_depreciation]
[Ο όρος πάγια στοιχεία για απόσβεση (fixed assets for depreciation) αναφέρεται στα πάγια περιουσιακά στοιχεία που υπόκεινται σε απόσβεση, δηλαδή εκείνα που χρησιμοποιούνται από την επιχείρηση στις δραστηριότητές της και έχουν περιορισμένη ωφέλιμη διάρκεια ζωής.]
[Documentation fixed_assets_for_depreciation]
[The term fixed assets for depreciation (fixed assets for depreciation) refers to the assets that are subject to depreciation, that is, those that are referred by the company to its activities and have a limited useful life.]
"""
    due_to_operating_expenses = """"[Τεκμηρίωση due_to_operating_expenses]
[Ο όρος "due to operating expenses" μπορεί να αποδοθεί στα ελληνικά ως "λόγω λειτουργικών εξόδων" ή "εξαιτίας λειτουργικών εξόδων".]
[Χρησιμοποιείται για να περιγράψει δαπάνες ή υποχρεώσεις που προκύπτουν από την καθημερινή λειτουργία μιας επιχείρησης.]
[Μπορεί να αναφέρεται σε λόγους για τους οποίους μειώνονται τα έσοδα ή το κέρδος, π.χ. "Η μείωση των καθαρών κερδών οφείλεται στα υψηλά λειτουργικά έξοδα.]
[Documentation due_to_operating_expenses]
[It is used to describe expenses or liabilities arising from the day-to-day running of a business.]
[It can refer to reasons why revenue or profit is falling, e.g. "The decrease in net profits is due to high operating expenses.]
"""

class MetaReturnTotalCapitalEmployed:
    """## Return:  meta data"""

    net_profit = """[Τεκμηρίωση net_profit]
[Στις επιχειρήσεις, το καθαρό εισόδημα ή τα καθαρά κέρδη είναι τα έσοδα μείον το κόστος πωληθέντων αγαθών, τα έξοδα και τους φόρους για μια λογιστική χρήση.]
[Documentation net_profit]
[In business, net income or net profit is revenue minus cost of goods sold, expenses, and taxes for an accounting year.]
"""
    net_sales = """[Τεκμηρίωση net_sales]
[Η αξία των πωλήσεων μιας οικονομικής μονάδας μετά την αφαίρεση των φόρων (πχ. ΦΠΑ), των επιστροφών, των εκπτώσεων και της αξίας των κατεστραμμένων προϊόντων]
[Documentation net_sales]
[The value of sales of an economic unit after deduction of taxes (e.g. VAT), returns, discounts and the value of damaged products]
"""
    interest = """[Τεκμηρίωση interest]
[Τόκος είναι η αποζημίωση σε χρήματα που είναι υποχρεωμένος να δώσει ο οφειλέτης στο δανειστή για ορισμένη ποσότητα χρηματικού δανείου που πήρε για συγκεκριμένη χρονική περίοδο.]
[Οι οικονομολόγοι συχνά αναφέρονται στον τόκο ως αμοιβή για τη χρησιμοποίηση χρηματικού κεφαλαίου, ή ως τιμή με την οποία χρεώνεται η χρήση κεφαλαίου. Ο λόγος του τόκου προς το κεφάλαιο λέγεται επιτόκιο. ]
[Documentation interest]
[Interest is the compensation in money that the debtor is obliged to give to the lender for a certain amount of money borrowed for a certain period of time.]
[Economists often refer to interest as a fee for the use of money capital, or as the price at which the use of capital is needed. The ratio of the interest to the principal is called the interest rate.]
"""
    tax_rate = """[Τεκμηρίωση tax_rate]
[Ο φορολογικός συντελεστής (tax_rate) είναι ένα ποσοστό που αντιπροσωπεύει το ποσό του φόρου που επιβάλλεται στα κέρδη μιας επιχείρησης ή ενός ατόμου. Εκφράζεται συνήθως ως δεκαδικός αριθμός ή ποσοστό.]
[Documentation tax_rate]
[The tax rate (tax_rate) is a percentage that represents the amount of tax levied on the profits of a business or an individual. It is usually expressed as a decimal number or percentage.]
"""
    total_capital = """[Τεκμηρίωση total_capital]
[ο συνολικό κεφάλαιο αναφέρεται στο άθροισμα όλων των οικονομικών πόρων που διαθέτει μία επιχείρηση ή ένα άτομο, συμπεριλαμβανομένων ιδίων κεφαλαίων και δανειακού κεφαλαίου. Περιλαμβάνει όλα τα στοιχεία ενεργητικού που χρησιμοποιούνται για την επίτευξη κέρδους,]
[όπως μετρητά, επενδύσεις, ακίνητα και εξοπλισμό. Είναι ένας σημαντικός δείκτης για την οικονομική κατάσταση και τη χρηματοδοτική ικανότητα.]
[Documentation total_capital]
[Total capital refers to the sum of all financial resources available to a business or an individual, including equity and debt capital. It includes all assets used to make a profit.]
[such as cash, investments, property and equipment. It is an important indicator of financial status and financial capacity.]
"""


def __str__(self):
    attributes = [
        self.circulating_assets,
        self.short_term_liabilities,
        self.available_cash,
        self.forecast_daily_expenses,
        self.requirements,
    ]
    return "\n\n".join(map(str, attributes))