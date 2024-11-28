from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI  # Use ChatOpenAI for chat models like GPT-4
from langchain.chains import LLMChain

import pprint
import os
import openai

# Get the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define your prompt template
prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Informazioni oggetto dell’estrazione:
    1.	Campi puntuali:
    o	ISIN (se e dove presente)
    o	SRI – indicatore sintetico di riscbìhio (va da 1 a 7)
    o	RHP – orizzonte di detenzione raccomandato
    o	NOME DEL PRODOTTO
    o	NOME DELL’EMITTENTE
    2.	Campi testuali:
    o	Target market
    3.	Campi tabellari (Hint: sarebbe opportuno, prima di interrogare un LLM, estrarre la tabella in maniera strutturata):

    Esempio di output atteso (documento KID1.pdf):
    text:
    documento contenente le informazioni chiave - allegato di seguito vengono riportate le caratteristiche dellopzione di investimento sottostante il prodotto in relazione a: obiettivi dellinvestimento, investitori di riferimento, indicatore di rischio, scenari di performance, costi totali, impatto annuale sul rendimento (riy) nonch il periodo di detenzione raccomandato. lopzione di investimento rappresenta la scelta di investire il 100% del capitale nella singola opzione. prodotto: unit personal private (tariffe ux64 - ux65 - ux66 - ux67 - ux68) opzione di investimento: core balanced opportunity emittente: fineco asset management isin: lu0690021539 codice interno: 13457 combinazione cnp di appartenenza: oicr flessibili/bilanciati data di realizzazione del documento: 06/02/2024 state per acquistare un'opzione d'investimento che non  semplice e pu essere di difficile comprensione. obiettivi dell'opzione di investimento: il comparto investir almeno il 50% del suo patrimonio in titoli di debito e strumenti finanziari ad essi collegati direttamente o indirettamente tramite oicr di tipo aperto. il comparto pu investire fino al 50% del suo patrimonio in titoli azionari e strumenti finanziari ad essi collegati, anche tramite altri oicr. investitori al dettaglio di riferimento dell'opzione di investimento: il fondo esterno  rivolto ai clienti aventi una buona conoscenza e/o esperienza dei mercati finanziari e assicurativi e una bassa tolleranza al rischio finanziario, i quali intendono investire il proprio capitale nel medio periodo accettando i possibili rischi di perdita connessi all'investimento finanziario. quali sono i rischi e qual  il potenziale rendimento? indicatore di rischio rischio pi basso rischio pi alto 1 2 3 4 5 6 7 l'indicatore di rischio presuppone che l'opzione d'investimento sia mantenuta per 5 anni. il rischio effettivo pu variare in misura significativa in caso di disinvestimento in una fase iniziale e la somma rimborsata potrebbe essere minore. pu non essere possibile disinvestire anticipatamente. potrebbe essere necessario sostenere notevoli costi supplementari per disinvestire anticipatamente. l'indicatore di rischio  un'indicazione orientativa del livello di rischio di questa opzione di investimento rispetto ad altre opzioni. esso esprime la probabilit che il prodotto subisca perdite monetarie a causa di movimenti sul mercato o a causa della nostra incapacit di pagarvi quanto dovuto. abbiamo classificato questa opzione di investimento al livello 2 su 7 che corrisponde alla classe di rischio basso. ci significa che le perdite potenziali dovute alla performance futura del prodotto sono classificate nel livello basso e che  molto improbabile che le cattive condizioni di mercato influenzino la capacit di cnp vita assicura s.p.a. di pagarvi quanto dovuto. scenari di performance il possibile rimborso dipender dallandamento futuro dei mercati, che  incerto e non pu essere previsto con esattezza. lo scenario sfavorevole, lo scenario moderato e lo scenario favorevole riportati sono illustrazioni basate sulla performance peggiore, la performance media e la performance migliore del prodotto negli ultimi 10 anni. nel futuro i mercati potrebbero avere un andamento molto diverso. lo scenario caso morte si basa sullo scenario moderato ed  calcolato considerando la percentuale di maggiorazione pi bassa. periodo di detenzione raccomandato: 5 anni esempio di investimento:  10.000 premio assicurativo [ 0] in caso di uscita dopo 1 anno in caso di uscita dopo 5 anni scenari - caso vita possibile rimborso al netto dei costi (rendimento medio annuo) minimo non esiste un rendimento minimo garantito. potreste perdere il vostro intero investimento o parte di esso. stress  7,670 ( -23.30 % )  7,410 ( -5.82 % ) sfavorevole  8,360 ( -16.36 % )  8,710 ( -2.73 % ) moderato  9,870 ( -1.26 % )  10,060 ( 0.13 % ) favorevole  10,940 ( 9.41 % )  10,500 ( 0.99 % ) scenario - caso morte possibile rimborso a favore dei vostri beneficiari al netto dei costi in caso di decesso dell'assicurato  10.180  10.270 le cifre riportate comprendono tutti i costi del prodotto in quanto tale, ma possono non comprendere tutti i costi da voi pagati al consulente o al distributore. le cifre non tengono conto della vostra situazione fiscale personale, che pu incidere anch'essa sull'importo del rimborso. lo scenario di stress indica quale potrebbe essere limporto rimborsato in circostanze di mercato estreme. lo scenario sfavorevole si  verificato per un investimento nell'opzione/parametro di riferimento idoneo tra il ottobre 2017 e il ottobre 2022. lo scenario moderato si  verificato per un investimento nell'opzione/parametro di riferimento idoneo tra il novembre 2015 e il novembre 2020. lo scenario favorevole si  verificato per un investimento nell'opzione/parametro di riferimento idoneo tra il aprile 2014 e il aprile 2019. allegato - unit personal private - ux64 - ux65 - ux66 - ux67 - ux68 - pagina 1 di 2 questo prodotto non  facilmente liquidabile. in caso di uscita da un investimento prima del periodo di detenzione raccomandato potrebbe essere necessario sostenere costi supplementari. quali sono i costi? la persona che fornisce consulenza sul prodotto o che lo vende potrebbe addebitare altri costi, nel qual caso fornir informazioni su tali costi, illustrandone limpatto sullinvestimento. andamento dei costi nel tempo le tabelle mostrano gli importi prelevati dallinvestimento per coprire diversi tipi di costi. tali importi dipendono dallentit dellinvestimento, dalla durata della detenzione del prodotto e dallandamento del prodotto. gli importi sono qui riportati a fini illustrativi e si basano su un importo esemplificativo dellinvestimento e su diversi possibili periodi di investimento. si  ipotizzato quanto segue:  nel primo anno recupero dellimporto investito (rendimento annuo dello 0%). per gli altri periodi di detenzione si  ipotizzato che il prodotto abbia la performance indicata nello scenario moderato;  10.000 euro di investimento. in caso di uscita dopo 1 anno in caso di uscita dopo 5 anni costi totali  425  1.702 incidenza annuale dei costi (*) 4,2% 3,2% ogni anno (*) dimostra come i costi riducano ogni anno il rendimento nel corso del periodo di detenzione. ad esempio, se luscita avviene nel periodo di detenzione raccomandato, si prevede che il rendimento medio annuo sar pari al 3,3% prima dei costi e al 0,1% al netto dei costi. una parte dei costi pu essere condivisa con la persona che vende il prodotto per coprire i servizi che fornisce. limporto vi verr comunicato in seguito. composizione dei costi costi una tantum di ingresso o di uscita incidenza annuale dei costi in caso di uscita dopo 5 anni percentuale dei costi prelevati dal premio pagato al momento della sottoscrizione costi di ingresso 0,0% dell'investimento percentuale dei costi prelevati dal vostro investimento prima che vi venga pagato. i costi di uscita costi di uscita sono indicati come "n/a" nella colonna successiva in quanto non si applicano se il prodotto  n/a conservato fino al periodo di detenzione raccomandato. costi correnti registrati ogni anno commissioni di gestione e percentuale del valore dell'investimento all'anno che tratteniamo ogni anno per la gestione dei altri costi amministrativi o di 3,2% vostri investimenti. si tratta di una stima basata sui costi effettivi dell'ultimo anno. esercizio percentuale del valore dellinvestimento allanno. si tratta di una stima dei costi sostenuti per costi di transazione lacquisto e la vendita degli investimenti sottostanti per il prodotto. limporto effettivo varier a 0,0% seconda di quanto viene acquistato e venduto. periodo di detenzione raccomandato dell'opzione di investimento: 5 anni. altre informazioni rilevanti nella sezione situazione fondi del sito www.gruppocnp.it sono disponibili le performance passate dell'oicr e le informazioni sulla loro modalit di calcolo. le performance sono riportate per gli ultimi 10 anni o per un minor periodo se non  disponibile una storicit pari a 10 anni e vengono aggiornate e pubblicate mensilmente. allegato - unit personal private - ux64 - ux65 - ux66 - ux67 - ux68 - pagina 2 di 2 cnp vita assicura s.p.a. societ soggetta a direzione e coordinamento di cnp assurances s.a. - sede legale: via arbe, 49 - 20125 milano - impresa autorizzata allesercizio delle assicurazioni con decreto del min. dellindustria, del commercio e dellartigianato n. 18240 del 28/07/1989 pubblicato sulla g.u. n. 186 del 10/08/1989 - capitale sociale euro 247.000.000,00 i.v. - reg. delle imprese di milano, c. fiscale e p. iva 09269930153 - iscr. allalbo delle imprese di assicurazione e riassicurazione al n. 1.00081 - pec cnpvita_assicura@legalmail.it - www.gruppocnp.it
    output:
    -	ISIN: LU0690021539
    -	SRI: 2
    -	RHP: 5
    -	NOME DEL PRODOTTO: Unit Personal Private
    -	NOME DELL’EMITTENTE: Fineco Asset Management
    -	TARGET MARKET: il Fondo Esterno è rivolto ai clienti aventi una buona conoscenza e/o esperienza dei mercati finanziari e assicurativi e una bassa tolleranza al rischio finanziario, i quali intendono investire il proprio capitale nel medio periodo accettando i possibili rischi di perdita connessi all'investimento finanziario.
    -	SCENARI DI PERFORMANCE A RHP: 
    o	stress -5.82%, 
    o	sfavorevole -2.73%, 
    o	moderato 0.13%. 
    o	favorevole 0.99%




    Document Text:
    {text}
    """
)

# Initialize the ChatOpenAI model (use ChatOpenAI for GPT-4)
llm = ChatOpenAI(api_key=openai.api_key, model="gpt-4")

# Combine the prompt with the model using LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Read document text from the file
with open("./processed_texts/KID2.txt", "r") as file:
    document_text = file.read()

# Get the results from LangChain using invoke instead of run
result = chain.invoke({"text": document_text})

# Print the extracted information
pprint.pprint(result)