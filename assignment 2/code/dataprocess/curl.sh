awk '!/^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$/ && NF > 0 {
    diff = $2 - $1;
    diffs[NR] = diff;
}
END {
    asort(diffs);
    n = length(diffs);
    median = (n % 2 == 1) ? diffs[int(n / 2) + 1] : (diffs[n / 2] + diffs[n / 2 + 1]) / 2;
    median_ms = median * 1000;  
    print "Median:", median_ms;
}' sgp1.iperf.comnet-student.eu.txt



awk '!/^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$/ && NF > 0 {
    diff = $2 - $1;
    sum += diff;
    count++;
}
END {
    average = (sum / count) * 1000;  
    print "Mean:", average;
}' sgp1.iperf.comnet-student.eu.txt


awk '!/^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$/ && NF > 0 {
    diff = $2 - $1;
    diffs[NR] = diff;
}
END {
    asort(diffs);
    n = length(diffs);
    percentiles_75 = diffs[int(n * 0.75) + 1] * 1000;  
    percentiles_25 = diffs[int(n * 0.25) + 1] * 1000;  
    percentile_diff = (percentiles_75 - percentiles_25); 
    print "Percentiles_75:", percentiles_75;
    print "Percentiles_25:", percentiles_25;
    print "Diff:", percentile_diff;
}' sgp1.iperf.comnet-student.eu.txt