select distinct tittel, navn, rollenavn
from SpillerRolle
join Teaterstykke using(stykkeid)
join Person using(pid)
