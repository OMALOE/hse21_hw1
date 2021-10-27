# Домашнее задание №1

Выполнил: Архипов Д. А., 2 группа

## Список команд

```
seqtk sample -s503 oil_R1.fastq 5000000 > sub1.fast
seqtk sample -s503 oil_R2.fastq 5000000 > sub2.fastq
fastqc sub1.fastq
fastqc sub2.fastq
fastqc sub1MP.fastq
fastqc sub2MP.fastq
multiqc .

platanus_trim sub1.fastq sub2.fastq
platanus_internal_trim sub1MP.fastq sub2MP.fastq

mkdir deleted //такие папки на сервере я делал, чтоб на всякий случай не удалять файлы. Мало ли...
mkdir trimmed
mv -t trimmed sub1.fastq.trimmed sub2.fastq.trimmed sub1MP.fastq.trimmed sub2MP.fastq.trimmed
mv -t deleted sub1.fastq sub2.fastq sub1MP.fastq sub2MP.fastq
cd trimmed
fastqc sub1.fastq.trimmed
fastqc sub2.fastq.trimmed
fastqc sub1MP.fastq.int_trimmed
fastqc sub1MP.fastq.int_trimmed
multiqc .

platanus assemble  -o Poil -t 8 -n 28 -f sub1.fastq.trimmed sub2.fastq.trimmed 2> asseble.log
platanus scaffold -c Poil_contig.fa -IP1 sub1.fastq.trimmed sub2.fastq.trimmed -OP2 sub1MP.fastq.int_trimmed sub2MP.fastq.int_trimmed 2> scaffold.log

platanus gap_close -c out_scaffold.fa -IP1 sub1.fastq.trimmed sub2.fastq.trimmed -OP2 sub1MP.fastq.int_trimmed sub2MP.fastq.int_trimmed 2> gap_close.log


head out_gapClosed.fa
echo scaffold1_cov232 > sn.lst
seqtk subseq out_gapClosed.fa sn.lst > longest.fa


```
## Скриншоты для изначальных ридов

![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/1.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/2.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/3.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/4.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/5.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/6.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/7.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/8.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/9.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/10.png?raw=true)

## Скриншоты подрезанных ридов

![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/21.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/22.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/23.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/24.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/25.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/26.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/27.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/28.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/29.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/30.png?raw=true)
![alt text](https://github.com/OMALOE/hse21_hw1/blob/main/imgs/31.png?raw=true)

## Ссылка на Google Colab
https://colab.research.google.com/drive/1JzAdv43LzZANkMB2LdbNriu7yWFtikB5?usp=sharing
