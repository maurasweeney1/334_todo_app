set terminal png size 900,400
set output "build_time_graph.png"
set title "Build Time Over Time"
set xlabel "Date"
set ylabel "Build Duration (seconds)"
set xdata time
set timefmt "%Y-%m-%d"
set format x "%b %d"
set xrange ["2026-04-20":"2026-04-26"]
set xtics rotate by -45
set grid
set key off
set style data linespoints
plot "build_time_log.txt" using 1:2 title "Build time (s)" lc rgb "#0077cc" lw 2 pt 7 ps 1
