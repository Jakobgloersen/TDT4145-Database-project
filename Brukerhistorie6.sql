select tittel, dato, count(billettid)
from Forestilling
join Teaterstykke using(stykkeid)
left join Billett using(fid)
group by fid
order by count(billettid) desc