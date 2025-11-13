#Working with Sets
from pyscript import display


Basketball = {'Enzo', 'Seth', 'Gurnoor', 'Juanico', 'Oscar'}
Band = {'Juanico','Erin', 'Matteo', 'Danni', 'Xidris'}

display(Basketball | Band, target="output") 
display(Basketball & Band, target="output")
display(Basketball, target="output")
display(Band, target="output")
display(Basketball ^ Band, target="output")