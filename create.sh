n=1;
max=31;
while [ "$n" -le "$max" ]; do
 hdfs dfs -mkdir "/FootballPosts/2020/12/$n"
  n=`expr "$n" + 1`;
done

