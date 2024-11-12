passenger=int(input('Enter the number of passenger:'))
dist=int(input('Enter the distance in KM:'))
inc=(passenger*80)
fuel=(dist/10)
cp=(fuel*70)
if inc>cp:
    print('The route is on profit:')
    profit=(inc-cp)
    print('The profit is:',profit)
else:
     print('The route is on loss:')
     loss=(cp-inc)
     print('The loss is:',loss)
