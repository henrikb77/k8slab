## lab 1

kubectl apply deployment som loggar

Ändra till 2 replicas och se att två poddar exekverar.

## lab 2
Exponera port via service med webserver som svarar på GET.

## lab 3

Introducera rolling upgrades. Visa att applikationen fortsätter svara vid uppgradering.

## lab 4
Introducera två dåliga endpoints. En som kraschar applikationen och en som låser applikationen. Anropa en i taget och visa att applikationen fortsätter svara trots att en replica startas om.

## lab 5 (visa bara)
Installera t ex flux och uppgradera via gitops.

## lab 6 autoskalning (visa bara)
Använd HPA. Peppra applikation med requests tills den skalar upp