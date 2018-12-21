#!/bin/bash

echo '=== Preparing datacards in root format ==='

DIR=$1/Node_SM
echo $DIR

text2workspace.py $DIR/hhbbgg_13TeV_DataCard.txt $DIR/hhbbgg_13TeV_DataCard.root -m 125 --X-nuisance-group-function 'theory' '0.5'

cd $DIR

printf '\n=== Start fitting ==\n\n'

combine -M FitDiagnostics -d hhbbgg_13TeV_DataCard.root -S 0 &> MaxLikelihood_stat.txt

combine -M FitDiagnostics -d hhbbgg_13TeV_DataCard.root -S 0  --saveWorkspace --saveShapes --saveNormalization &> MaxLikelihood_stat.txt

printf '\n=====\n\n'

combine -M Asymptotic -d hhbbgg_13TeV_DataCard.root -t -1 --run blind --expectSignal 1 -m 125 -n SM_13TeV_3ab -S 0

echo '== 3.1) Finished stat only limits'

head  Limit_stat.txt

#printf '\n=====\n\n'

#combine -M Asymptotic -d hhbbgg_13TeV_DataCard.root -t -1  --run blind --expectSignal 1 -m 125 -n SM_13TeV_3ab &> Limit.txt

#echo '== 3.2) Finished full limits'

#head  Limit.txt

#printf '\n=====\n\n'

cd -

printf '\n== END ===\n\n'

