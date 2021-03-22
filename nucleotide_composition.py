#!/usr/bin/env python
# coding: utf-8

# In[1]:


# name of the input file
filename = "nad4L.fasta"


# In[2]:


# opening the input file
infile = open(filename, "r")


# In[3]:


# read the file 
sequence = infile.read().rstrip()
print(sequence)


# In[4]:


# close the input file
infile.close()


# In[5]:


# counting the sequence length 
seqlen = len(sequence)
# print(seqlen)


# In[6]:


# needed sequence output
print("Sequence length:" , seqlen)


# In[7]:


# finding frequency of A
freqA = (sequence.count("A") / seqlen)
print(freqA)


# In[8]:


# needed freqA output
print("Freq of A:" , freqA)


# In[9]:


# finding frequency of C
freqC = (sequence.count("C") / seqlen)
print(freqC)


# In[10]:


# needed freqC output
print("Freq of C:" , freqC)


# In[11]:


# finding frequency of G
freqG = (sequence.count("G") / seqlen)
print(freqG)


# In[12]:


# needed freqG output
print("Freq of G:" , freqG)


# In[13]:


# finding frequency of T
freqT = (sequence.count("T") / seqlen)
print (freqT)


# In[14]:


# needed freqT output
print("Freq of T:" , freqT)


# In[15]:


# finding frequency of G+C
freqGC = ((sequence.count("G") + sequence.count("C")) / seqlen)
print(freqGC)


# In[16]:


# needed G+C output 
print("G+C content:" , freqGC)


# In[17]:


# checking frequencies all sum to 1
print(freqA + freqC + freqG + freqT)

